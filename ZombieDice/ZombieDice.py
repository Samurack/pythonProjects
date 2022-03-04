#ZombieDice.py
import random 
from dice import dice
from greenDie import greenDie
from yellowDie import yellowDie
from redDie import redDie
from player import player
from roll import roll

ShotGun = []
Brains = []
typesOfDice = [greenDie(),yellowDie(),redDie()]

bagOfDice = dice.loadDiceBag(typesOfDice)
usersDiceInHand = 0
diceInHand = []
diceInHand = player(diceInHand).selectDice(bagOfDice) 

nextRoll = roll(diceInHand)
print(diceInHand)
ShotGun, Brains, rolls = nextRoll.rollDice(ShotGun,Brains)
# print("diceInHand", diceInHand)
# print("ShotGun", ShotGun)
# print("Brains", Brains)
