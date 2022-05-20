from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import requests
import re
from usersCards import usersCards
from prebuiltCards import prebuiltCards
from bs4 import BeautifulSoup

app = Flask(__name__)

# https://learnpython.com/blog/python-requirements-file/
# https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-portal%2Cvscode-deploy%2Cterminal-bash%2Cdeploy-instructions-azportal%2Cdeploy-instructions-zip-azcli
# https://portal.azure.com/#@jmichaelrollins89gmailcom.onmicrosoft.com/resource/subscriptions/062bd048-67c7-4556-8c26-ce4bdb2133a7/resourcegroups/MTG_Testing_Resource_Group/providers/Microsoft.Web/sites/Mtg-Search-For-Deck/appServices
# https://search.brave.com/search?q=install+beautiful+soup&source=desktop
# https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   collectionUrl = request.form.get('collectionUrl')
   deckUrl = request.form.get('deckUrl')

   if collectionUrl and deckUrl:
       prebuiltCardsClass = prebuiltCards(deckUrl)
       prebuiltListOfCards = prebuiltCardsClass.getCards()

       usersCardsClass = usersCards(collectionUrl)
       usersListOfCards = usersCardsClass.getCards()
       sameCards = []
       for card in usersListOfCards:
         for deckCard in prebuiltListOfCards: 
            if card.rstrip() == deckCard.rstrip():
               sameCards.append(card.rstrip())
       print(sameCards)
       return render_template('hello.html', sameCards = sameCards)
   else:
       print('Request for hello page received with no collectionUrl or collectionUrl -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()