#ZombieDice.py
import random
from flask import Flask, render_template #https://realpython.com/python-web-applications/
from os import system
from ZombieDice.dice import dice
from ZombieDice.greenDie import greenDie
from ZombieDice.yellowDie import yellowDie
from ZombieDice.redDie import redDie
from ZombieDice.santaDie import santaDie
from ZombieDice.hunkDie import hunkDie
from ZombieDice.hottieDie import hottieDie
from ZombieDice.player import player
from ZombieDice.roll import roll

####################################################################################################################################
# https://python.land/virtual-environments/virtualenv
# https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
####################################################################################################################################
PlayerOneShotGun = []
PlayerOneBrains = []
PlayerTwoShotGun = []
PlayerTwoBrains = []
diceInHand = []
typesOfDice = [greenDie(6),yellowDie(4),redDie(3)]
usersDiceInHand = 0
playerOne = player("One", diceInHand, PlayerOneBrains, PlayerOneShotGun, typesOfDice)
playerTwo = player("Two", diceInHand, PlayerTwoBrains, PlayerTwoShotGun, typesOfDice)
# bagOfDice = dice.loadDiceBag(typesOfDice) #load the initial bag the users will pull from
won = "No"


app = Flask(__name__)

@app.route("/")
def home():
    global won
    global PlayerOneBrains
    global PlayerOneShotGun
    global PlayerTwoBrains
    global PlayerTwoShotGun

    POB = len(PlayerOneBrains)
    POSG = len(PlayerOneShotGun)
    PTB = len(PlayerTwoBrains)
    PTSG = len(PlayerTwoShotGun)
    bagOfDice = dice.loadDiceBag(typesOfDice) #load the initial bag the users will pull from

    return render_template("home.html", bagOfDice=bagOfDice, PlayerOneBrains=POB, PlayerOneShotGun=POSG, PlayerTwoBrains=PTB, PlayerTwoShotGun=PTSG)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)