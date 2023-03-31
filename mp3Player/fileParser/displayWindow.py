import time
import os
from tkinter import *
import fileParser as parser
import userYamlFile as userFile
from tkinter import filedialog

pipeline_file = "" #open("pipeline.yml", "r")                                                 #Opening a text file

path = '\\defaultTemplates' #userFile.browseFiles()

yaml_templates = []#parser.read_template_files(path)
evaluation_lines = []#parser.read_pipeline_file(pipeline_file, yaml_templates)
position = 0
class List: #https://www.geeksforgeeks.org/create-table-using-tkinter/
      
    def __init__(self,root):
        global position
        # code for creating table
        for i in range(len(evaluation_lines)):
            list_evaluation_lines.insert(i, evaluation_lines[i])
            if "Potential issue parameters are:" in evaluation_lines[i]:
                list_evaluation_lines.itemconfig(i, bg="#bdc1d6") #######################this hightlights the items in the list
            if "You are using a version one template please update for a better evaluation" in evaluation_lines[i]:
                list_evaluation_lines.itemconfig(i, bg="#bdc1d6") #######################this hightlights the items in the list

        list_evaluation_lines.pack(padx=10,pady=10,fill="both",expand=True) #https://www.tutorialspoint.com/python/tk_listbox.htm

def openLoadWindow(): #https://www.delftstack.com/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/
    global path
    global yaml_templates
    global evaluation_lines
    global pipeline_file

    path = os.getcwd() + path
    pipeline_file = open(userFile.browseFiles())
    buttonExample.destroy()
    yaml_templates = parser.read_template_files(path)
    evaluation_lines = parser.read_pipeline_file(pipeline_file, yaml_templates)
    lbl_label.pack()
    list_evaluation_lines = List(root)

root = Tk()
buttonExample = Button(root, 
              text="Choose Yaml File",
              command=openLoadWindow)
buttonExample.place(relx=0.5, rely=0.5, anchor=CENTER)


MyLeftPos = (root.winfo_screenwidth() - 800) / 2 #https://www.skotechlearn.com/2020/06/tkinter-window-position-size-center-screen-in-python.html --- Process(3):
myTopPos = (root.winfo_screenheight() - 850) / 2

lbl_label = Label( #https://www.instructables.com/Create-a-Simple-Python-Text-Editor/
    text="Potential Template Issues",
    background="light gray",
    foreground="black",
    width="590",
    height="1"
)

root.geometry( "%dx%d+%d+%d" % (800,800, MyLeftPos, myTopPos))

root.title("Template Evaluator")

# Adjust size 
list_evaluation_lines = Listbox(root)
# list_evaluation_lines = List(root)
root.mainloop()
