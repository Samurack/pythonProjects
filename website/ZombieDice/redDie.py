#ZombieDice.py
from ZombieDice.dice import dice

class redDie(dice):
	def __init__(self,NOD):
		self.NOD = NOD
		sides = ["Brains","Shotgun","Shotgun","Shotgun","Footprints","Footprints"]
		super().__init__(sides,"red",NOD) #NOD = 3

	def showColor(self):
		return "red"