import requests
from bs4 import BeautifulSoup
import re
import time
from browser_history.browsers import Brave #https://browser-history.readthedocs.io/en/latest/usage.html#using-the-cli     https://realpython.com/python-lists-tuples/
from datetime import datetime as dt
from rentalProperty import Apartment
from pullWebsiteInformation import pullWebsiteInformation


def getPrice(simpleWebsite):
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
      # nb_price_links = soup.find_all(attrs={"class": "_3UEVw _3lM_H _2mxoW _2nzTc _1befF _3KYTJ V358y _4TP_c pNFNm _2nR4s _2Zxdp"}) #https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
      individual_nb_price_links = soup.find_all(attrs={"data-tid": "listing-price"}) #https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
      print(len(individual_nb_price_links))
      priceList = []

      for link in range(len(individual_nb_price_links)): #https://www.geeksforgeeks.org/python-arrays/
         priceList.append(individual_nb_price_links[link].text)

   return priceList

def getAddress(simpleWebsite):
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
      nb_address_links = soup.find_all(attrs={"data-tid": "address"}) #https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
      bedNbathList = []

      for link in range(len(nb_address_links)): #https://www.geeksforgeeks.org/python-arrays/
         bedNbathList.append(nb_address_links[link].text)
   return bedNbathList

def setupApartments(listOfApartments, website, listOfPrices, listOfAddresses):
   if len(listOfPrices) == len(listOfAddresses):
      length = len(listOfPrices)
      for x in range(length):
         oneApartment = Apartment(website, listOfPrices[x], listOfAddresses[x])
         listOfApartments.append(oneApartment.setApartmentInformation())
   return listOfApartments

apartmentList = []

# webSiteURL = "https://www.rentals.com/Utah/Ogden/max-price-1000/"
# pricesLinks = pullWebsiteInformation(webSiteURL, "data-tid", "listing-price")
# addressesLinks = pullWebsiteInformation(webSiteURL, "data-tid", "address")
# prices = pricesLinks.getInformationByAttrs()
# addresses = addressesLinks.getInformationByAttrs()
# apartmentsInObjectList = setupApartments(apartmentList, webSiteURL, prices, addresses)

# webSiteURL = "https://www.rentler.com/places-for-rent/ut/orem/?maxprice=1500&minprice=600"
# pricesLinks = pullWebsiteInformation(webSiteURL, "class", "price")
# addressesLinks = pullWebsiteInformation(webSiteURL, "class","address")
# prices = pricesLinks.getInformationByAttrs()
# addresses = addressesLinks.getInformationByAttrs()
# apartmentsInObjectList = setupApartments(apartmentList, webSiteURL, prices, addresses)

# webSiteURL = "https://homes.ksl.com/rent/search/ut/orem/minprice-600/maxprice-1200"
# pricesLinks = pullWebsiteInformation(webSiteURL, "data-test","price")
# addressesLinks = pullWebsiteInformation(webSiteURL, "data-test","address")
# prices = pricesLinks.getInformationByAttrs()
# addresses = addressesLinks.getInformationByAttrs()
# apartmentsInObjectList = setupApartments(apartmentList, webSiteURL, prices, addresses)

webSiteURL = "https://www.apartmentguide.com/apartments/Utah/Orem/"
pricesLinks = pullWebsiteInformation(webSiteURL, "data-tid","price")
addressesLinks = pullWebsiteInformation(webSiteURL, "data-tid","address")
prices = pricesLinks.getInformationByAttrs()
addresses = addressesLinks.getInformationByAttrs()
apartmentsInObjectList = setupApartments(apartmentList, webSiteURL, prices, addresses)
print("List of places")
for aList in apartmentsInObjectList:
   print(aList)
# print(apartmentsInObjectList)
###################################################
# https://pypi.org/project/browserhistory/
###################################################