import requests
from bs4 import BeautifulSoup
import re
import time
from browser_history.browsers import Brave #https://browser-history.readthedocs.io/en/latest/usage.html#using-the-cli     https://realpython.com/python-lists-tuples/
from datetime import datetime as dt

class Apartment(): #http://buildandteach.com/wp-content/uploads/2019/03/Screen-Shot-2019-03-17-at-8.24.07-PM.png
                    #https://docs.python.org/3/tutorial/classes.html
   def __init__(self, website, price, address):
      self.website = website
      self.price = price
      self.address = address

   def setApartmentInformation(self):
      vals = (self.website, self.price, self.address)
      return vals

###################################################
# https://pypi.org/project/browserhistory/
###################################################