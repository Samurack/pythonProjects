#ZombieDice.py
from ZombieDice.dice import dice

class greenDie(dice):
	def __init__(self, NOD):
		self.NOD = NOD
		sides = ["Brains","Brains","Brains","Shotgun","Footprints","Footprints"]
		super().__init__(sides,"green",NOD) #NOD = 6

	def showColor(self):
		return "green"