# These are the imports to be made
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 
chrome_options = Options()  
chrome_options.add_argument("--headless")  

# path of the chromedriver we have just downloaded
PATH = r"D:\code\tiffany\CollegeWebScraper\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(PATH, chrome_options=chrome_options) # to open the browser

# url of google news website
url = 'https://collegescorecard.ed.gov/search/?search=Brigham%20Young%20University'

# to open the url in the browser
driver.get(url)
# Xpath you just copied
time.sleep(2.4)

news_path = '//*[@class="nameLink"]' ########################https://www.guru99.com/xpath-selenium.html
# to get that element
link = driver.find_elements_by_xpath(news_path)
for l in link:
	print(l.get_attribute("href"))