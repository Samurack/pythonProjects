import random 

class roll():
	def __init__(self, diceInHand):
		self.diceInHand = diceInHand

	def rollDice(self,ShotGunArray,BrainsArray):
		roll = []
		print(len(self.diceInHand))
		for die in self.diceInHand:
			singleRoll = random.choice(die.getSides())
			if singleRoll == "Brains":
				BrainsArray.append(die)
				self.diceInHand.remove(die)
			if singleRoll == "Shotgun":
				ShotGunArray.append(die)
				self.diceInHand.remove(die)
			print(singleRoll)
			roll.append(singleRoll)
		return ShotGunArray, BrainsArray, roll