import time
# opening a text file
pipeline_file = open("pipeline.yml", "r")
yaml_templates = ["cloudfoundry-deploy.yml", "cf-deploy-job.yml"]

def read_template_file(file_to_read, user_parameters_list):

    required_parameters = []
    read_lines = False
    required_file_parameters = file_to_read.readlines()

    for line in required_file_parameters:
        if line in ['\n', '\r\n']:
            read_lines = False
        elif "condition" in line.strip():
            read_lines = read_lines
        elif read_lines:
            if "#" not in line.strip()[:1]:
                required_parameters.append(line.split(":")[0].strip())
                # print(line.split(":")[0].strip())  # If you want to see each line being parsed uncomment
        elif "parameters:" in line.strip():
            read_lines = True
    check_required_parameters(required_parameters, user_parameters_list)
    file_to_read.close()


def read_pipeline_file(file_to_read):
    required_parameters = []
    read_lines = False
    required_file_parameters = file_to_read.readlines()
    first_yaml = True
    lines = 0
    global yaml_templates
    for line in required_file_parameters:
        lines = lines + 1
        if line[0] == '#':
            ignore=1 #Ignore this line because the code is commented out
        elif "templates/" in line:
            index = line.find('#') #stores the index of a substring or char
            print("Line", lines, line[:index])
            print(" ----- ", "Using a version one template please update", "  ----- ")
            print()
        else:
            for x in yaml_templates:
                if x in line:
                    first_yaml = False
                    yaml_to_read = open(x, "r")
                    index = line.find('#') #stores the index of a substring or char
                    print("Line", lines, " Checking ", line[:index])
           
        # if line[0] == '#':
        #     ignore=1
        # elif "azure-java-mvn-docker/azure-java-mvn-docker.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("azure-java-mvn-docker.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "cloudfoundry-deploy/cloudfoundry-deploy.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("cf-deploy-job.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "cloudfoundry-deploy/cf-deploy-job.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("cf-deploy-job.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "docker-build/docker-build.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("docker-build.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif ".netcore-build/.netcore-build.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open(".netcore-build.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "java-mvn-build/java-mvn-build.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("java-mvn-build-required.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "javascript-npm-build/javascript-npm-build.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("javascript-npm-build.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "docker-image-promotion/docker-image-promotion.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("docker-image-promotion.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "download-build-artifact/download-build-artifact.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("download-build-artifact.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "extract-files/extract-files.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("extract-files.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "azure-artifactory-promotion/azure-artifactory-promotion.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("azure-artifactory-promotion.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "templates/azure-java-mvn.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("azure-java-mvn.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "marklogic/marklogic-build.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("marklogic-build.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "marklogic/marklogic-deploy.yml" in line:
        #     first_yaml = False
        #     yaml_to_read = open("marklogic-deploy.yml", "r")
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, " Checking ", line[:index])
        # elif "templates/" in line:
        #     index = line.find('#') #stores the index of a substring or char
        #     print("Line", lines, line[:index])
        #     print(" ----- ", "Using a version one template please update", "  ----- ")
        #     print()

        if not first_yaml:
            if line in ['\n', '\r\n']:
                read_lines = False
                first_yaml = True
                read_template_file(yaml_to_read, required_parameters)
                required_parameters = []
            elif "condition" in line.strip():
                read_lines = False
                first_yaml = True
                read_template_file(yaml_to_read, required_parameters)
                required_parameters = []
            elif "parameters:" in line.strip():
                read_lines = True
            elif read_lines:
                if "#" not in line.strip()[:1]:
                    required_parameters.append(line.split(":")[0].strip())
                    # print(line.split(":")[0].strip())  # If you want to see each line being parsed uncomment

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
            print("Potential issue parameters are: ")
            for y in number_of_issues:
                    print(" - ", y, "")
            print()

read_pipeline_file(pipeline_file)
