#ZombieDice.py
import random

class player():
   def __init__(self, diceInHand):
      self.numberOfDice = 3
      self.diceInHand = diceInHand

   def getUsableDice(self):
      return self.diceInHand

   #User should have three dice they are using is their selection isn't full add that many more dice into the bag
   def selectDice(self, bagOfDice):
      if len(self.diceInHand) < self.numberOfDice:
         numberOfDiceNeeded = self.numberOfDice - len(self.diceInHand)
         for i in range(numberOfDiceNeeded):
            random.shuffle(bagOfDice)
            self.diceInHand.append(bagOfDice[0])
            bagOfDice.pop()
      return self.diceInHand