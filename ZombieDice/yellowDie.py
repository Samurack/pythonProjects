#ZombieDice.py
from dice import dice

class yellowDie(dice):
	def __init__(self,NOD):
		self.NOD = NOD
		sides = ["Brains","Brains","Shotgun","Shotgun","Footprints","Footprints"]
		super().__init__(sides,"yellow",NOD) #NOD = 4

	def showColor(self):
		return "yellow"