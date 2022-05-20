import requests
import re
from usersCards import usersCards
from prebuiltCards import prebuiltCards
from bs4 import BeautifulSoup

####################################################
# User needs to make part of his collection visible
# Then get public collection URL from this link
# https://store.tcgplayer.com/collection
# Next provide a mtg deck link and BAM!
####################################################

DeckURL = "https://www.mtgtop8.com/event?e=30989&d=441017&f=ST"
usersCardsUrl = "https://store.tcgplayer.com/collection/view/434613"

prebuiltCardsClass = prebuiltCards(DeckURL)
prebuiltListOfCards = prebuiltCardsClass.getCards()

usersCardsClass = usersCards(usersCardsUrl)
usersListOfCards = usersCardsClass.getCards()


# for result in prebuiltListOfCards:
# 	print(result)


for card in usersListOfCards:
	for deckCard in prebuiltListOfCards: 
		if not card.rstrip() == deckCard.rstrip():
			print("You are missing this card")
			print(card)