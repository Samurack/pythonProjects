#prebuiltCards.py
import requests
import re
from bs4 import BeautifulSoup

class prebuiltCards():
	def __init__(self, baseUrl):
		self.baseUrl = baseUrl

	def getBaseUrl(self):
		return self.baseUrl

	def getCards(self):
		page = requests.get(self.baseUrl)
		soup = BeautifulSoup(page.content, "html.parser")
		preBuiltHtml = soup.findAll("span", class_="L14")
		prebuiltListOfCards = []
		for result in preBuiltHtml:
			prebuiltListOfCards.append(str(result.getText()))
		return prebuiltListOfCards