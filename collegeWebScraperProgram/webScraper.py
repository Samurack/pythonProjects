import requests, re, time #https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests
import tkinter as tk
import time
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup #https://stackoverflow.com/questions/11783875/importerror-no-module-named-bs4-beautifulsoup
# from browser_history.browsers import Brave  #https://pypi.org/project/browserhistory/
from datetime import datetime as dt
from Createcollege import CollegeClass
from pullWebsiteInformation import pullWebsiteInformation
from addToExcel import writeToExcel
from readFromExcel import readingFromExcel
from PIL import ImageTk,Image   #https://stackoverflow.com/questions/8863917/importerror-no-module-named-pil

#https://pypi.org/project/selenium/
#https://stackoverflow.com/questions/34509198/no-module-named-openpyxl-python-3-4-ubuntu
#https://stackoverflow.com/questions/8863917/importerror-no-module-named-pil
#https://stackoverflow.com/questions/11783875/importerror-no-module-named-bs4-beautifulsoup
#https://pypi.org/project/webdriver-manager/

############################################################################
# https://browser-history.readthedocs.io/en/latest/usage.html#using-the-cli
# https://realpython.com/python-lists-tuples/
# https://collegescorecard.ed.gov/
# https://pypi.org/project/browserhistory/
############################################################################

collegeNames = []
CollegeUrls = []
listOfColleges = []

searchUrl = "https://collegescorecard.ed.gov/search/?search="
college_url_path = '//*[@class="nameLink"]'
costXpath = ".//*[@id=\"school-avg-cost\"]//*[contains(@class,\"display-2 navy-text font-weight-bold\")]"

root= tk.Tk()
excelWorkbook = "testingExcel.xlsx"
currentSpreadsheet = "Colleges"
photo = "please-wait-flat-icon-graphic-vector-24176629.jpg"
img = ImageTk.PhotoImage(Image.open(photo)) #https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

label1 = tk.Label(root, text= "What's the name of the Current Colleges Spreadsheet?")
canvas1.create_window(200, 10, window=label1)

entry1 = tk.Entry (root)
entry1.insert(0, "Colleges")
canvas1.create_window(200, 30, window=entry1)


def setSheetInformation():
   global excelWorkbook
   global currentSpreadsheet
   global searchUrl
   global college_url_path
   global costXpath
   global collegeNames
   global CollegeUrls
   global listOfColleges
   global canvas1
   global photo
   global canvas1
   global img
   canvas1.delete('all')
   canvas1.create_image(200, 30, image=img)
   time.sleep(2.4)
   excelWorkbook = askopenfilename() # show an "Open" dialog box and return the path to the selected file
   currentSpreadsheet = entry1.get()

   excelObject = readingFromExcel(excelWorkbook, currentSpreadsheet) 
   collegeNames = excelObject.updateExcelSheet()
   for collegeName in collegeNames:
      urlCollegeName = collegeName.replace(" ", "%20")
      collegeSearch = searchUrl + urlCollegeName
      collegeLinks = pullWebsiteInformation(collegeSearch, college_url_path)
      listOfSearchOptions = collegeLinks.getListOfInformationByAttrs()
      print(listOfSearchOptions)

      if isinstance(listOfSearchOptions, list):
         for l in listOfSearchOptions:
            if l.text == collegeName:
               CollegeUrls.append(l.get_attribute("href"))
               costLink = pullWebsiteInformation(l.get_attribute("href"), costXpath)
               cost = costLink.getInformationByAttrs()
               nextCollege = CollegeClass(collegeName,cost)
               addCollege = nextCollege.setCollegeInformation()
               listOfColleges.append(nextCollege)
      else:
         if listOfSearchOptions.text == collegeName:
            CollegeUrls.append(listOfSearchOptions.get_attribute("href"))
            costLink = pullWebsiteInformation(listOfSearchOptions.get_attribute("href"), costXpath)
            cost = costLink.getInformationByAttrs()
            nextCollege = CollegeClass(collegeName,cost)
            addCollege = nextCollege.setCollegeInformation()
            listOfColleges.append(nextCollege)


   excelSheet = writeToExcel(excelWorkbook, currentSpreadsheet, listOfColleges)

   print("Update Excel Spreadsheet")
   excelSheet.updateExcelSheet()
   canvas1.delete('all')
   label1 = tk.Label(root, text= "The Spreadsheet has been updated")
   canvas1.create_window(200, 100, window=label1)
   # Button for closing
   exit_button = tk.Button(root, text="Exit", command=root.destroy)
   canvas1.create_window(200, 60, window=exit_button)

button1 = tk.Button(text='Which Excel Workbook do you want to use?', command=setSheetInformation)
canvas1.create_window(200, 60, window=button1)

root.mainloop()