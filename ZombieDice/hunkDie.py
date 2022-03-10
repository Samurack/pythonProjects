#ZombieDice.py
from dice import dice

class hunkDie(dice):
	def __init__(self):
		sides = ["DoubleBrains","Shotgun","Shotgun","DoubleShotgun","Footprints","Footprints"]
		super().__init__(sides,"white",1)

	def showColor(self):
		return "white"