#ZombieDice.py
from dice import dice

class hottieDie(dice):
	def __init__(self):
		sides = ["Brains","Shotgun","Shotgun","Footprints","Footprints","Footprints"]
		super().__init__(sides,"pink",1)

	def showColor(self):
		return "pink"