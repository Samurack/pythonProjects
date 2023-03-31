import time
import os
from tkinter import *

pipeline_file = open("pipeline.yml", "r")                                                 #Opening a text file

PATH = 'D:\\Python_desktop_application\\fileParser\\defaultTemplates'

yaml_templates = []
evaluation_lines = []

#Read all the file names for the example template files
def read_template_files():                                                                
    global yaml_templates
    global PATH
    
    for i in os.listdir(PATH):
        yaml_templates.append(str(i))

#Read the template file to see what the required parameters are
def read_template_file(file_to_read, user_parameters_list):

    required_parameters = []
    read_lines = False
    required_file_parameters = file_to_read.readlines()

    for line in required_file_parameters:
        if line.strip() in ['\n', '\r\n', '']:                                          #If we hit a new line we know we need to stop reading
            read_lines = False
        elif "condition" in line.strip():                                               #If we find a condition we know it's the end of the parameters section
            read_lines = read_lines
        elif read_lines:
            if "#" not in line.strip()[:1]:
                required_parameters.append(line.split(":")[0].strip())
                # print(line.split(":")[0].strip())                                     #If you want to see each line being parsed uncomment
        elif "parameters:" in line.strip():
            read_lines = True
    check_required_parameters(required_parameters, user_parameters_list)
    file_to_read.close()

#Read the users pipeline file looking for the parameters the user has put in the file
#Also looks for each time that the user calls a template file
def read_pipeline_file(file_to_read):
    required_parameters = []
    read_lines = False
    required_file_parameters = file_to_read.readlines()
    first_yaml = True
    lines = 2
    global yaml_templates
    #print(yaml_templates)
    for line in required_file_parameters:
        lines = lines + 1
        if line[0] == '#':
            ignore=1                                                                  #Ignore this line because the code is commented out
        elif "templates/" in line:
            index = line.find('#')                                                    #stores the index of a substring or char
            evaluation_lines.append("Line" + str(lines) + str(line[:index]))
            evaluation_lines.append(" ----- " + "Using a version one template please update" + "  ----- ")
            evaluation_lines.append("")
            # print("Line", lines, line[:index])
            # print(" ----- ", "Using a version one template please update", "  ----- ")
            # print()
        else:
            for x in yaml_templates:
                if x in line:
                    first_yaml = False
                    yaml_to_read = open("defaultTemplates/" + x, "r")                #reads the file from the files folder
                    index = line.find('#')                                           #stores the index of a substring or char
                    evaluation_lines.append("Line" + str(lines) + " Checking " + str(line[:index]))
                    #print("Line", lines, " Checking ", line[:index])

        if not first_yaml:                                                           #until we find the first yaml file we don't want to look at new lines 
            if line.strip() in ['\n', '\r\n']:                                       #A new line should indicate the end of the parameters section if not remove the line for now
                read_lines = False
                first_yaml = True
                read_template_file(yaml_to_read, required_parameters)
                required_parameters = []
            elif "condition" in line.strip():                                        #A condition should indicate the end of the parameters section                                     
                read_lines = False
                first_yaml = True
                read_template_file(yaml_to_read, required_parameters)
                required_parameters = []
            elif "parameters:" in line.strip():                                      #A parameters should indicate the beginning of the parameters section
                read_lines = True
            elif read_lines:
                if "#" not in line.strip()[:1]:
                    required_parameters.append(line.split(":")[0].strip())
                    # print(line.split(":")[0].strip())                              #If you want to see each line being parsed uncomment

    # closing a file
    return required_parameters


def check_required_parameters(parameter_list, users_parameter_list):
    number_of_issues = []
    if len(parameter_list) > 0:
        # checking condition for string found or not
        for x in parameter_list:
            if x not in users_parameter_list:
                number_of_issues.append(x)
        if len(number_of_issues) > 0:
            evaluation_lines.append("Potential issue parameters are: ")
            #print("Potential issue parameters are: ")
            for y in number_of_issues:
                    evaluation_lines.append(" - " +  str(y) + "")
                    #print(" - ", y, "")
            evaluation_lines.append("")
            #print()

read_template_files()
read_pipeline_file(pipeline_file)

class Table: #https://www.geeksforgeeks.org/create-table-using-tkinter/
      
    def __init__(self,root):
          
        # code for creating table
        for i in range(len(evaluation_lines)):
            self.e = Entry(root, width=100, fg='blue',
                           font=('Arial',16,'bold'))
              
            self.e.grid(row=i, column=1)
            self.e.insert(END, evaluation_lines[i])

root = Tk()

t = Table(root)
root.mainloop()