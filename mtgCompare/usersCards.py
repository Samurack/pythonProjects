#usersCards.py
import requests
import re
from bs4 import BeautifulSoup

class usersCards():
	def __init__(self, baseUrl):
		self.baseUrl = baseUrl

	def getBaseUrl(self):
		return self.baseUrl

	def getCards(self):
		cardsPage = requests.get(self.baseUrl)
		cardsSoup = BeautifulSoup(cardsPage.content, "html.parser")
		#https://stackoverflow.com/questions/38252434/beautifulsoup-to-find-a-link-that-contains-a-specific-word
		#https://stackoverflow.com/questions/28073833/beautiful-soup-div-with-class-and-id-both
		cardsHTML = cardsSoup.findAll("a", target="_blank", href=re.compile("https://www.tcgplayer.com/product"))
		usersListOfCards = []
		for result in cardsHTML:
			usersListOfCards.append(str(result.getText()))
		return usersListOfCards