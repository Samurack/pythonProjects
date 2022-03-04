# # importing the libraries
# from bs4 import BeautifulSoup
# import requests
# # import csv

# # change hosts path according to your OS
# hosts_path = "C:\Windows\System32\drivers\etc\hosts"
# # localhost's IP
# redirect = "127.0.0.1"

# # Step 1: Sending a HTTP request to a URL
# # url = "https://www.instructables.com/craft/projects/"
# # Make a GET request to fetch the raw HTML content
# while True:
#       with open(hosts_path, 'r') as file:
#          content = file.read()
#          print(content)
#          html_content = requests.get(content).text

#          # Step 2: Parse the html content
#          soup = BeautifulSoup(html_content, "lxml")
#          # print(soup.prettify()) # print the parsed data of html
#          print(soup.title.string)

#          for a in soup.find_all('a'):
#             if "Cooking" in a:
#                print("One Instance which is: ", a)
#                file.write(redirect + " " + website + "\n")

# #Import libraries
# import time
# from datetime import datetime as dt
# #Windows host file path
# hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
# redirect="127.0.0.1"
# #Add the website you want to block, in this list
# websites=["https://www.pinterest.com/", "www.pinterest.com","pinterest.com", "www.DeviantArt.com", "DeviantArt.com", "https://www.DeviantArt.com/"]
# while True:
#    #Duration during which, website blocker will work
#    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,10):
#       # print ("Sorry Not Allowed...")
#       with open(hostsPath,'r+') as file:
#          print ("Block Site...")
#          content = file.read()
#          for site in websites:
#             if site in content:
#                pass
#             else:
#                file.write(redirect+" "+site+"\n")
#    else:
#       with open(hostsPath,'r+') as file:
#          print ("Open Site...")
#          content = file.readlines()
#          file.seek(0)
#          for line in content:
#             if not any(site in line for site in websites):
#                file.write(line)
#                file.truncate()
#       print ("Allowed access!")
# time.sleep(5)
#Import libraries
import time
from datetime import datetime as dt
#Windows host file path
hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
#Add the website you want to block, in this list
websites=["https://www.pinterest.com/", "www.pinterest.com","pinterest.com", "www.DeviantArt.com", "DeviantArt.com", "https://www.DeviantArt.com/"]
while True:
   #Duration during which, website blocker will work
   with open(hostsPath,'r+') as file:
      print ("Block Site...")
      content = file.read()
      for site in websites:
         if site in content:
            pass
         else:
            file.write(redirect+" "+site+"\n")
time.sleep(5)