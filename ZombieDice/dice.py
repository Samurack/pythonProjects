#ZombieDice.py

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
			for die in range(dieType.numberOfDice()): #add a die method for the amount of dice in the specified dices color
				typesOfDice.append(dieType)
		return typesOfDice