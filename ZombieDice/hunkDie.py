#ZombieDice.py
from dice import dice

class hunkDie(dice):
	def __init__(self,NOD):
		self.NOD = NOD
		sides = ["DoubleBrains","Shotgun","Shotgun","DoubleShotgun","Footprints","Footprints"]
		super().__init__(sides,"white",NOD) #NOD = 1

	def showColor(self):
		return "white"