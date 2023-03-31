# These are the imports to be made
import time
from selenium import webdriver
#options to add as arguments
from selenium.webdriver.chrome.options import Options

###################################################################################################
# https://docs.python.org/3/tutorial/classes.html
# http://buildandteach.com/wp-content/uploads/2019/03/Screen-Shot-2019-03-17-at-8.24.07-PM.png
# https://www.geeksforgeeks.org/how-to-build-web-scraping-bot-in-python/
# https://pypi.org/project/browserhistory/
# https://www.geeksforgeeks.org/how-to-build-web-scraping-bot-in-python/
###################################################################################################

class pullWebsiteInformation(): 
   def __init__(self, simpleWebsite, xPath):
      self.simpleWebsite = simpleWebsite
      self.xPath = xPath

   def getInformationByAttrs(self): 
      chrome_options = Options()  
      chrome_options.add_argument("--headless")  

      # path of the chromedriver we have just downloaded
      ###################This needs to match your version of Chrome installed on your computer
      PATH = r"D:\code\pythonProjects\tiffany\CollegeWebScraper\chromedriver_win32\chromedriver" ####################https://chromedriver.chromium.org/downloads
      driver = webdriver.Chrome(PATH, chrome_options=chrome_options) # to open the browser

      driver.get(self.simpleWebsite)
      time.sleep(2.4)
      news_path = (self.xPath)
      link = driver.find_element_by_xpath(news_path)

      # to read the text from that element
      return link.text

   def getListOfInformationByAttrs(self):#, hrefUser): 
      chrome_options = Options()  
      chrome_options.add_argument("--headless")  

      # path of the chromedriver we have just downloaded
      PATH = r"D:\code\pythonProjects\tiffany\CollegeWebScraper\chromedriver_win32\chromedriver"
      driver = webdriver.Chrome(PATH, chrome_options=chrome_options) # to open the browser

      driver.get(self.simpleWebsite)
      time.sleep(2.4)
      news_path = (self.xPath)
      links = driver.find_element("xpath", news_path)
      # userRef = link.get_attribute(hrefUser)
      # to read the text from that element
      return links