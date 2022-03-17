import random

class roll():
	def __init__(self, diceInHand):
		self.diceInHand = diceInHand

	def rollDice(self,ShotGunArray,BrainsArray,bagOfDice):
		roll = []
		removeDie = []
		if self.diceInHand[0].showColor() == "white":
			random.shuffle(self.diceInHand)

		for die in self.diceInHand:
			if die.showColor() == "pink":
				hottiePosition = self.diceInHand.index(die) #https://www.adamsmith.haus/python/answers/how-to-find-the-position-of-an-element-in-an-array-in-python#:~:text=Use%20list.,position%20of%20value%20in%20list%20.
				del self.diceInHand[hottiePosition] #https://www.programiz.com/python-programming/array
				self.diceInHand.append(die)

		for die in self.diceInHand:
			singleRoll = random.choice(die.getSides())
			if die.showColor() == "pink" and singleRoll == "Shotgun":
				BrainsArray = self.rollDiceHottieShotgun(BrainsArray)
			if singleRoll == "Brains":
				die, BrainsArray, removeDie = self.rollDiceBrains(die, BrainsArray, removeDie)
			if singleRoll == "HottieBrains":
				die, BrainsArray, removeDie = self.rollDiceBrains(die, BrainsArray, removeDie)
			if singleRoll == "Shotgun":
				die, ShotGunArray, removeDie = self.rollDiceShotgun(die, ShotGunArray, removeDie)
			if singleRoll == "DoubleBrains":
				die, BrainsArray, removeDie = self.rollDiceDoubleBrains(die, BrainsArray, removeDie)
			if singleRoll == "DoubleShotgun":
				die, BrainsArray, ShotGunArray, removeDie, bagOfDice = self.rollDiceDoubleShotgun(die, BrainsArray, ShotGunArray, removeDie, bagOfDice)
			print(singleRoll)
			roll.append(singleRoll)

		for remove in removeDie:
			self.diceInHand.remove(remove)
		return ShotGunArray, BrainsArray, roll

	def rollDiceBrains(self, Die, Brains, Remove):
		Brains.append(Die)
		Remove.append(Die)
		return Die, Brains, Remove

	def rollDiceShotgun(self, Die, ShotGun, Remove):
		ShotGun.append(Die)
		Remove.append(Die)
		return Die, ShotGun, Remove

	def rollDiceDoubleBrains(self, Die, Brains, Remove):
		Brains.append(Die)
		Brains.append(Die)
		Remove.append(Die)
		return Die, Brains, Remove

	def rollDiceDoubleShotgun(self, Die, Brains, ShotGun, Remove, bagAllDice):
		ShotGun.append(Die)
		ShotGun.append(Die)
		for dice in Brains:
			if dice.showColor() == "pink": #If the hottie is in the brains array she is removed the hunk saved her!
				print("The hunk Saved the Hottie! Sorry you lost her brains!")
				hottiePosition = Brains.index(dice) #https://www.adamsmith.haus/python/answers/how-to-find-the-position-of-an-element-in-an-array-in-python#:~:text=Use%20list.,position%20of%20value%20in%20list%20.
				bagAllDice.append(dice)
				del Brains[hottiePosition] #https://www.programiz.com/python-programming/array
		Remove.append(Die)
		return Die, Brains, ShotGun, Remove, bagAllDice

	def rollDiceHottieShotgun(self, Brains):
		for oneDie in Brains:
			if oneDie.showColor() == "white":
				doubleBrainsPosition = Brains.index(oneDie)
				del Brains[doubleBrainsPosition] #https://www.programiz.com/python-programming/array
				doubleBrainsPosition = Brains.index(oneDie)
				del Brains[doubleBrainsPosition] #https://www.programiz.com/python-programming/array
		print("The Hottie Saved the hunk! Sorry you lost his brains!")
		return Brains