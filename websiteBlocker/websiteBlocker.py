import requests
from bs4 import BeautifulSoup
import re
import time
from browser_history.browsers import Brave #https://browser-history.readthedocs.io/en/latest/usage.html#using-the-cli     https://realpython.com/python-lists-tuples/
from datetime import datetime as dt

f = Brave()
outputs = f.fetch_history()
his = outputs.histories
# print(his)
def ListWebSites(history):
   for website in history:
      print(website[1])

hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
#Windows host file path
redirect="127.0.0.1"
#Add the website you want to block, in this list
websitesToBlock=[]
keyWords=[]
warningList=[]
websitesChecked=[]
newWebsitesChecked=[]

with open("D:\websiteBlocker\keyWords.txt") as file:
    for line in file:
       keyWords.append(line.rstrip().lower())

with open("D:\websiteBlocker\warningList.txt") as file:
    for line in file:
       warningList.append(line.rstrip().lower())

with open("D:\websiteBlocker\websites.txt") as file:
    for line in file:
       websitesChecked.append(line.rstrip().lower())

def evaluateWebSite(history):
   global websitesToBlock
   global keyWords
   global warningList
   global websitesChecked
   for website in history:
      firstSimpleWebsite = website[1]

      if "https" in firstSimpleWebsite:
         pass
      elif "www" in firstSimpleWebsite:
        firstSimpleWebsite = "https://" + firstSimpleWebsite
      else:
         firstSimpleWebsite = "https://www." + firstSimpleWebsite

      simpleWebsite = firstSimpleWebsite.split(".com", 1)[0]
      simpleWebsite = simpleWebsite + ".com"
      if simpleWebsite in websitesChecked:
         pass
      else:
         print('Checking Site ' + simpleWebsite)
         websitesChecked.append(simpleWebsite)
         newWebsitesChecked.append(simpleWebsite)
         try:
            response = requests.get(simpleWebsite, timeout=20)
         except requests.exceptions.Timeout as err: 
            response = requests.get("https://www.google.com")
            response.status_code = 408
            print("The check for this website timed out!")
         except:
            print('Error fetching page ' + simpleWebsite)

         if response.status_code != 200:
            pass
         else:
            soup = BeautifulSoup(response.content, 'html.parser') #https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/

            # images = soup.find_all('img', {'src':re.compile('.jpg')}) ##########################https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-8.php

            nb_links_length = len(soup.find_all('a'))
            nb_links = soup.find_all('a')

            print(f"There are {nb_links_length} links in this page")

            for link in nb_links:
               lowerLink = str(link).lower()
               for warning in warningList:
                  if findWholeWord(warning)(lowerLink):
                     print("We detected the warning word " + warning + " in this link ")
                     print(lowerLink)
                     blockSite = input("Should we block the site? y or n: ")#https://www.geeksforgeeks.org/taking-input-in-python/
                     if blockSite.lower() == "y":
                       print("You have opted to block the site")
                       if simpleWebsite not in websitesToBlock:
                         addSitesToArray(simpleWebsite)
                         blockSitesInArray(websitesToBlock)
                     else:
                        print("Ok we are not blocking this site")
                        pass

               for keyWord in keyWords:                  
                  if findWholeWord(keyWord)(lowerLink):
                     print("We detected the warning word " + keyWord + " in this link ")
                     print(lowerLink)
                     blockSite = input("Should we block the site? y or n: ")#https://www.geeksforgeeks.org/taking-input-in-python/
                     if blockSite.lower() == "y":
                       print("You have opted to block the site")
                       if simpleWebsite not in websitesToBlock:
                         addSitesToArray(simpleWebsite)
                         blockSitesInArray(websitesToBlock)
                     else:
                        print("Ok we are not blocking this site")
                        pass

def addSitesToArray(simpleWebsite):
   global websitesToBlock
   websitesToBlock.append(simpleWebsite)
   print(simpleWebsite)
   if 'https://' in simpleWebsite:
      website = simpleWebsite.replace('https://','')
      print(website)
      websitesToBlock.append(website)
      if 'www.' in website:
         website = website.replace('www.','')
         print(website)
         websitesToBlock.append(website)

def findWholeWord(w):
   return re.compile(r'\b({0})\b'.format(re.escape(w)), flags=re.IGNORECASE).search #https://stackoverflow.com/questions/5319922/python-check-if-word-is-in-a-string

def blockSitesInArray(webss):
   with open(hostsPath,'r+') as file:
      content = file.read()
      for site in webss:
         if site in content:
            print("Site " + site + " being blocked already")
            pass
         else:
            print("Attempting to block site " + site)
            file.write(redirect+" "+site+"\n")

def writeWebsitesCheckedToFile():
   global newWebsitesChecked
   print("Checking in websites ")
   file1 = open('D:\websiteBlocker\websites.txt', 'w')
   for website in newWebsitesChecked:
      file1.writelines(website + "\n")
   file1.close()
   print("All Websites are logged")
   time.sleep(5)


evaluateWebSite(his)
writeWebsitesCheckedToFile()

###################################################
# https://pypi.org/project/browserhistory/
###################################################