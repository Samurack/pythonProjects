import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime as dt

response = requests.get("https://www.instructables.com/")
if response.status_code != 200:
   print("Error fetching page")
   exit()
else:
   soup = BeautifulSoup(response.content, 'html.parser') #https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/

images = soup.find_all('img', {'src':re.compile('.jpg')}) ##########################https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-8.php

nb_links_length = len(soup.find_all('a'))
nb_links = soup.find_all('a')

keyWords=["Teachers", "Outside", "RGB"]

print(f"There are {nb_links_length} links in this page")
for link in nb_links:
   for keyWord in keyWords:
      if keyWord in str(link):
         print(link)
         print("---------------------------")


# #Windows host file path
# hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
# redirect="127.0.0.1"
# #Add the website you want to block, in this list
# websites=["https://www.pinterest.com/", "www.pinterest.com","pinterest.com", "www.DeviantArt.com", "DeviantArt.com", "https://www.DeviantArt.com/"]
# while True:
#    #Duration during which, website blocker will work
#    with open(hostsPath,'r+') as file:
#       print ("Block Site...")
#       content = file.read()
#       for site in websites:
#          if site in content:
#             pass###################################################################Here we will evaluate the website for malicious content
#          else:
#             file.write(redirect+" "+site+"\n")
# time.sleep(5)