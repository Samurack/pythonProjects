#ZombieDice.py
from dice import dice

class greenDie(dice):
	def __init__(self):
		sides = ["Brains","Brains","Brains","Shotgun","Footprints","Footprints"]
		super().__init__(sides,"green",6)
