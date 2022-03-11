#ZombieDice.py
import random
from os import system
from dice import dice
from greenDie import greenDie
from yellowDie import yellowDie
from redDie import redDie
from santaDie import santaDie
from hunkDie import hunkDie
from hottieDie import hottieDie
from player import player
from roll import roll
#Initial game setup
PlayerOneShotGun = []
PlayerOneBrains = []
PlayerTwoShotGun = []
PlayerTwoBrains = []
diceInHand = []
expansion = input("Are we playing the Hunk and Hottie expansion? y/n ")

if expansion == "y":
	typesOfDice = [greenDie(6),yellowDie(2),redDie(3),hottieDie(1),hunkDie(1)]
else:
	typesOfDice = [greenDie(6),yellowDie(4),redDie(3)]

usersDiceInHand = 0
playerOne = player("One", diceInHand, PlayerOneBrains, PlayerOneShotGun, typesOfDice)
playerTwo = player("Two", diceInHand, PlayerTwoBrains, PlayerTwoShotGun, typesOfDice)
bagOfDice = dice.loadDiceBag(typesOfDice) #load the initial bag the users will pull from

won = "No"
while won == "No":
	playerOne.userTurn(bagOfDice)
	bagOfDice = []
	bagOfDice = dice.loadDiceBag(typesOfDice) #load the initial bag the users will pull from
	if(len(PlayerOneBrains) >= 13):
		print("PlayerOneBrains", len(PlayerOneBrains))
		print("PlayerOneBrains", len(PlayerTwoBrains))
		if len(PlayerOneBrains) == len(PlayerTwoBrains):
			input("There's a Tie We need to play a tie round")
		else:
			print("Congratulations PlayerOne you have won!")
			won = "Yes"

	playerTwo.userTurn(bagOfDice)
	if(len(PlayerTwoBrains) >= 13):
		print("PlayerOneBrains", len(PlayerOneBrains))
		print("PlayerOneBrains", len(PlayerTwoBrains))
		if len(PlayerOneBrains) == len(PlayerTwoBrains):
			input("There's a Tie We need to play a tie round")
		else:
			print("Congratulations PlayerTwo you have won!")
			won = "Yes"
	bagOfDice = []
	bagOfDice = dice.loadDiceBag(typesOfDice) #load the initial bag the users will pull from

print("Thanks for playing Player One! Your final score was", len(PlayerOneBrains), "Brains!")
print("Thanks for playing Player Two! Your final score was", len(PlayerTwoBrains), "Brains!")