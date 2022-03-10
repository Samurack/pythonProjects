#ZombieDice.py
from dice import dice

class redDie(dice):
	def __init__(self):
		sides = ["Brains","Shotgun","Shotgun","Shotgun","Footprints","Footprints"]
		super().__init__(sides,"red",3)

	def showColor(self):
		return "red"