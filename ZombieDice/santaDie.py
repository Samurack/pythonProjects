#ZombieDice.py
from dice import dice

class santaDie(dice):
	def __init__(self):
		sides = ["Brains","DoubleShotgun","DoubleBrains","Helmet","EnergyDrink","Footprints"]
		super().__init__(sides,"christmasRed",1)

	def showColor(self):
		return "christmasRed"