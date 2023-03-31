import requests, re, time
from bs4 import BeautifulSoup
from browser_history.browsers import Brave  
from datetime import datetime as dt
from Createcollege import CollegeClass
from pullWebsiteInformation import pullWebsiteInformation
from addToExcel import writeToExcel
############################################################################
# https://browser-history.readthedocs.io/en/latest/usage.html#using-the-cli
# https://realpython.com/python-lists-tuples/
# https://collegescorecard.ed.gov/
# https://pypi.org/project/browserhistory/
############################################################################

collegeNames = ["Brigham Young University", "Brigham Young University-Idaho"]
CollegeUrls = []
listOfColleges = []

searchUrl = "https://collegescorecard.ed.gov/search/?search="
college_url_path = '//*[@class="nameLink"]'
costXpath = ".//*[@id=\"school-avg-cost\"]//*[contains(@class,\"display-2 navy-text font-weight-bold\")]"

for collegeName in collegeNames:
   urlCollegeName = collegeName.replace(" ", "%20")
   collegeSearch = searchUrl + urlCollegeName
   collegeLinks = pullWebsiteInformation(collegeSearch, college_url_path)
   listOfSearchOptions = collegeLinks.getListOfInformationByAttrs()
   print(listOfSearchOptions)
   for l in listOfSearchOptions:
      if l.text == collegeName:
         CollegeUrls.append(l.get_attribute("href"))
         costLink = pullWebsiteInformation(l.get_attribute("href"), costXpath)
         cost = costLink.getInformationByAttrs()
         nextCollege = CollegeClass(collegeName,cost)
         addCollege = nextCollege.setCollegeInformation()
         listOfColleges.append(nextCollege)

excelSheet = writeToExcel("testingExcel.xlsx", "Colleges", listOfColleges)

print("Update Excel Spreadsheet")
excelSheet.updateExcelSheet()