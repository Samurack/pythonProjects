#ZombieDice.py
import random #https://stackoverflow.com/questions/473973/shuffle-an-array-with-python-randomize-array-item-order-with-python

class dice():
	def __init__(self, sides, color, totalNumberOfDice):
		self.sides = sides
		self.color = color
		self.totalNumberOfDice = totalNumberOfDice

	def getSides(self):
		return self.sides

	def numberOfDice(self):
		return self.totalNumberOfDice

	def colorOfDie(self):
		return self.color

	def loadDiceBag(diceList):
		typesOfDice = []
		for dieType in diceList: #for all types of dice in list
			for die in range(dieType.numberOfDice()):
				typesOfDice.append(dieType)
		random.shuffle(typesOfDice)
		return typesOfDice