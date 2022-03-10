import random 

class roll():
	def __init__(self, diceInHand):
		self.diceInHand = diceInHand

	def rollDice(self,ShotGunArray,BrainsArray):
		roll = []
		removeDie = []
		for die in self.diceInHand:
			singleRoll = random.choice(die.getSides())
			if singleRoll == "Brains":
				BrainsArray.append(die)
				removeDie.append(die)
			if singleRoll == "Shotgun":
				ShotGunArray.append(die)
				removeDie.append(die)
			print(singleRoll)
			roll.append(singleRoll)
		for remove in removeDie:
			self.diceInHand.remove(remove)
		return ShotGunArray, BrainsArray, roll