import time
import os
from tkinter import *

pipeline_file = open("pipeline.yml", "r")                                                 #Opening a text file

yaml_templates = []
evaluation_lines = []
original_template = []
################################################################
#Read all the file names for the example template files
################################################################
def read_template_files(path):
    global yaml_templates

    for root, dirs, files in os.walk(path):
        for file in files:
            yaml_templates.append(os.path.join(root,file
    return yaml_templates


################################################################
# Read the template file to see what the required parameters are
################################################################
def read_template_file(file_to_read, user_parameters_list, evaluation_line):
    required_parameters = []
    read_lines = False
    required_file_parameters = file_to_read.readlines()

    for line in required_file_parameters:
        if line.strip() in ['\n', '\r\n', '']:                                           #If we hit a new line we know we need to stop reading
            read_lines = False
        elif "condition" in line.strip():                                                #If we find a condition we know it's the end of the parameters section
            read_lines = read_lines
        elif read_lines:
            if "#" not in line.strip()[:1]:
                required_parameters.append(line.split(":")[0].strip())
        elif "parameters:" in line.strip():
            read_lines = True
    check_required_parameters(required_parameters, user_parameters_list, evaluation_line)
    file_to_read.close()
    return required_parameters

####################################################################################################################
# Set the yaml file to compare against the users file
# make sure we remove any comments
# set the line, and template we are checking so we can show the user
####################################################################################################################
def find_yaml_file(yaml_File_from_list, template_call, line_num):
    global evaluation_lines
    yaml_to_read = open(yaml_File_from_list, "r")                                      #reads the file from the files folder
    index = template_call.find('#')                                                    #stores the index of a substring or char
    evaluation_line = ("Line " + str(line_num) + " Checking " + str(template_call[:index]))
    return yaml_to_read, evaluation_line

####################################################################################################################
# Create a section that looks at the version of a template that we are using and tells you if you are out of date# 
# Read the users pipeline file looking for the parameters the user has put in the file
# Also looks for each time that the user calls a template file
####################################################################################################################
def read_pipeline_file(file_to_read, yaml_templates):
    required_parameters = []
    required_file_parameters = file_to_read.readlines()
    read_parameters = False
    line_number = 0
    global evaluation_lines, original_template
    for line in required_file_parameters:
        original_template.append(line)
        line_number = line_number + 1
        if line[0] == '#':
            ignore = True                                                             #Ignore this line because the code is commented out
        elif "templates/" in line:
            index = line.find('#')                                                    #stores the index of a substring or char
            evaluation_lines.append("Line " + str(line_number) + str(line[:index]))
            evaluation_lines.append(" ----- " + "Using a version one template please update" + "  ----- ")
            evaluation_lines.append("----------------------------------------------------------------------------------------------")
            read_parameters = False
        else:
            if "- template:" in line.strip():
                for x in yaml_templates:
                    if x.rsplit("\\",1)[1] in line.rsplit("/",1)[1]:
                        read_parameters = True
                        yaml_to_read, evaluation_line = find_yaml_file(x, line, line_number)

        if read_parameters:                                                                             #until we find the first yaml file we don't want to look at new lines 
            if line.strip() in ['\n', '\r\n'] or line.strip() == "" or "condition" in line.strip():     #A new line should indicate the end of the parameters section if not remove the line for now
                read_parameters = False
                read_template_file(yaml_to_read, required_parameters, evaluation_line)
                required_parameters = []
            else:
                if "#" not in line.strip()[:1] and "parameters:" not in line.strip():
                    required_parameters.append(line.split(":")[0].strip())
    if len(evaluation_lines) == 0:
        evaluation_lines.append("Your Yaml file looks right as rain. Congradulations!")
    return evaluation_lines

################################################################
# Check the required parameters against the 
# parameters the +user has
################################################################
def check_required_parameters(parameter_list, users_parameter_list, evaluation_line):
    number_of_issues = []
    if len(parameter_list) > 0:
        # checking condition for string found or note
        for x in parameter_list:
            if x not in users_parameter_list:
                number_of_issues.append(x)
        if len(number_of_issues) > 0:
            evaluation_lines.append(evaluation_line)
            evaluation_lines.append("Potential issue parameters are: ")
            for y in number_of_issues:
                    evaluation_lines.append(" - " +  str(y) + "")
            evaluation_lines.append("----------------------------------------------------------------------------------------------")
