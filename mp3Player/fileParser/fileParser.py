import time
import os
from tkinter import *

#pipeline_file = open("pipeline.yml", "r")                                                 #Opening a text file

yaml_templates = []
original_template = []
base_required_parameters = []

################################################################
# Read all the file names for the example template files
################################################################
def read_template_files(path):
    global yaml_templates

    for root, dirs, files in os.walk(path):
        for file in files:
            yaml_templates.append(os.path.join(root,file))

    return yaml_templates

################################################################
# Read the template file to see what the required parameters are
################################################################
def read_template_file(file_to_read):
    default_required_parameters = []                                                      #The refernce template file will provide the required parameters for the template call
    read_lines = False
    required_file_parameters = file_to_read.readlines()
    for line in required_file_parameters:
        if line.strip() in ['\n', '\r\n', '']:                                           #If we hit a new line we know we need to stop reading
            read_lines = False
        elif "condition" in line.strip():                                                #If we find a condition we know it's the end of the parameters section
            read_lines = read_lines
        elif read_lines:
            if "#" not in line.strip()[:1]:
                default_required_parameters.append(line.split(":")[0].strip())
        elif "parameters:" in line.strip():
            read_lines = True
    file_to_read.close()
    return default_required_parameters

####################################################################################################################
# Set the yaml file to compare against the users file
# make sure we remove any comments
# set the line, and template we are checking so we can show the user
####################################################################################################################
def find_yaml_file(yaml_File_from_list, template_call):
    yaml_to_read = open(yaml_File_from_list, "r")                                      #reads the file from the files folder
    index = template_call.find('#')                                                    #stores the index of a substring or char
    return yaml_to_read

####################################################################################################################
# Create a section that looks at the version of a template that we are using and tells you if you are out of date# 
# Read the users pipeline file looking for the parameters the user has put in the file
# Also looks for each time that the user calls a template file
####################################################################################################################
def read_pipeline_file(file_to_read, yaml_templates):
    global original_template, base_required_parameters
    users_provided_parameters = []
    number_of_missing_Parameters = []
    required_file_parameters = file_to_read.readlines()
    read_parameters = False
    for line in required_file_parameters:
        original_template.append(line)
        if line[0] == '#':
            ignore = True                                                             #Ignore this line because the code is commented out
        elif "templates/" in line:
            # index = line.find('#')                                                    #stores the index of a substring or char
            original_template.append(" -----" + "You are using a version one template please update for a better evaluation" + "----- ")
            read_parameters = False
        else:
            if "- template:" in line.strip():
                for x in yaml_templates:
                    if x.rsplit("\\",1)[1] in line.rsplit("/",1)[1]:
                        read_parameters = True
                        yaml_to_read = find_yaml_file(x, line)
                        base_required_parameters = read_template_file(yaml_to_read)                                                    #Update the base_required_parameters from default template

        if read_parameters:                                                                                                            #Until we find the first yaml file we don't want to look at new lines 
            if line.strip() in ['\n', '\r\n'] or line.strip() == "" or "condition" in line.strip():                                    #A new line should indicate the end of the parameters section if not remove the line for now
                read_parameters = False
                number_of_missing_Parameters = check_required_parameters(users_provided_parameters, base_required_parameters)        #Check default parameters against user provided parameters
            else:
                if "#" not in line.strip()[:1] and "parameters:" not in line.strip():
                    users_provided_parameters.append(line.split(":")[0].strip())                                    #Get all user provided parameters
    number_of_missing_Parameters = check_required_parameters(users_provided_parameters, base_required_parameters)               #Check default parameters against user provided parameters

    if number_of_missing_Parameters == None:
        original_template.append("Your Yaml file looks right as rain. Congradulations!")

    return original_template

################################################################
# Check the required parameters against the 
# parameters the +user has
################################################################
def check_required_parameters(users_parameter_list, default_parameter_list):
    global original_template
    number_of_issues = []
    if len(users_parameter_list) > 0:
        # checking condition for string found or note
        for x in default_parameter_list:
            if x not in users_parameter_list:
                number_of_issues.append(x)
        if len(number_of_issues) > 0:
            original_template.append("----------------------------------------------------------")
            original_template.append("Potential issue parameters are: ")
            for y in number_of_issues:
                    original_template.append(" - " +  str(y) + "\n")
    original_template.append("\n")
    return number_of_issues
