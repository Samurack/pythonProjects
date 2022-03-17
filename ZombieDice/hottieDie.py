#ZombieDice.py
from dice import dice

class hottieDie(dice):
	def __init__(self,NOD):
		self.NOD = NOD
		sides = ["Shotgun"]
		# sides = ["HottieBrains","Shotgun","Shotgun","Footprints","Footprints","Footprints"]
		super().__init__(sides,"pink",NOD) #NOD = 1

	def showColor(self):
		return "pink"