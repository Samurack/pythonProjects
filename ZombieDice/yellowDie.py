#ZombieDice.py
from dice import dice

class yellowDie(dice):
	def __init__(self):
		sides = ["Brains","Brains","Shotgun","Shotgun","Footprints","Footprints"]
		super().__init__(sides,"yellow",4)