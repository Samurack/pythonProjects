import tkinter as tk
from CreateAntHillBuild import AntHillProject
from addToExcel import writeToExcel
from readFromExcel import ReadFromExcel
############################################################################
# https://datatofish.com/entry-box-tkinter/
############################################################################

root= tk.Tk()
excelWorkbook = "reposToMigrate.xlsx"
currentSpreadsheetGithub = "currentProjectsGithub"
currentSpreadsheetBitbucket = "currentProjectsBitbucket"
githubSpreadsheet = "github"
bitbucketSpreadsheet = "bitbucket"

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

label1 = tk.Label(root, text= "Which Excel Workbook do you want to use?")
canvas1.create_window(200, 10, window=label1)

entry1 = tk.Entry (root)
entry1.insert(0, "reposToMigrate.xlsx")
canvas1.create_window(200, 30, window=entry1)

label2 = tk.Label(root, text= "What's the name of the Current github Spreadsheet?")
canvas1.create_window(200, 60, window=label2)

entry2 = tk.Entry (root)
entry2.insert(0, "currentProjectsGithub")
canvas1.create_window(200, 80, window=entry2)

label3 = tk.Label(root, text= "What's the name of the github Spreadsheet?")
canvas1.create_window(200, 110, window=label3)

entry3 = tk.Entry (root)
entry3.insert(0, "github")
canvas1.create_window(200, 130, window=entry3)

label4 = tk.Label(root, text= "What's the name of the current bitbucket Spreadsheet?")
canvas1.create_window(200, 160, window=label4)

entry4 = tk.Entry (root)
entry4.insert(0, "currentProjectsBitbucket")
canvas1.create_window(200, 180, window=entry4)

label5 = tk.Label(root, text= "What's the name of the bitbucket Spreadsheet?")
canvas1.create_window(200, 210, window=label5)

entry5 = tk.Entry (root)
entry5.insert(0, "bitbucket")
canvas1.create_window(200, 230, window=entry5)

def setSheetInformation ():
   global excelWorkbook
   global currentSpreadsheetGithub
   global githubSpreadsheet
   global currentSpreadsheetBitbucket
   global bitbucketSpreadsheet
   excelWorkbook = entry1.get()
   currentSpreadsheetGithub = entry2.get()
   githubSpreadsheet = entry3.get()
   currentSpreadsheetBitbucket = entry4.get()
   bitbucketSpreadsheet = entry5.get()
   ReadExcelSheet = ReadFromExcel(excelWorkbook, currentSpreadsheetGithub)
   ALMProjects = ReadExcelSheet.readFromExcelSheet()
   excelSheet = writeToExcel(excelWorkbook, githubSpreadsheet, ALMProjects)
   print("Update github Excel Spreadsheet")
   excelSheet.updateExcelSheet()
   print("Updated github Excel Spreadsheet")

   ReadExcelSheet = ReadFromExcel(excelWorkbook, currentSpreadsheetBitbucket)
   ALMProjects = ReadExcelSheet.readFromExcelSheet()
   excelSheet = writeToExcel(excelWorkbook, bitbucketSpreadsheet, ALMProjects)
   print("Update bitbucket Excel Spreadsheet")
   excelSheet.updateExcelSheet()
   print("Updated bitbucket Excel Spreadsheet")
   canvas1.delete('all')
   label1 = tk.Label(root, text= "Excel Workbook Updated")
   canvas1.create_window(200, 10, window=label1)

button1 = tk.Button(text='Update Excel Workbook', command=setSheetInformation)
canvas1.create_window(200, 260, window=button1)

root.mainloop()