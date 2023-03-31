import requests
from bs4 import BeautifulSoup
import re
import time
from browser_history.browsers import Brave #https://browser-history.readthedocs.io/en/latest/usage.html#using-the-cli     https://realpython.com/python-lists-tuples/
from datetime import datetime as dt

class pullWebsiteInformation(): #http://buildandteach.com/wp-content/uploads/2019/03/Screen-Shot-2019-03-17-at-8.24.07-PM.png
                    #https://docs.python.org/3/tutorial/classes.html
   def __init__(self, simpleWebsite, htmlStructure, identifier):
      self.simpleWebsite = simpleWebsite
      self.htmlStructure = htmlStructure
      self.identifier = identifier

   def getInformationByAttrs(self):
      listOflinks = []

      try:
         response = requests.get(self.simpleWebsite, timeout=20)
      except requests.exceptions.Timeout as err: 
         response = requests.get("https://www.google.com")
         response.status_code = 408
         print("The check for this website timed out!")
      except:
         print('Error fetching page ' + self.simpleWebsite)
      
      if response.status_code != 200:
         pass
      else:
         soup = BeautifulSoup(response.text, 'html.parser') #https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/
         individual_nb_price_links = soup.find_all(attrs={self.htmlStructure: self.identifier}) #https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
         for link in range(len(individual_nb_price_links)): #https://www.geeksforgeeks.org/python-arrays/
            listOflinks.append(individual_nb_price_links[link].text)
      return listOflinks

###################################################
# https://pypi.org/project/browserhistory/
###################################################