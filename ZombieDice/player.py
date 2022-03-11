#ZombieDice.py
import random
from os import system
from roll import roll
from dice import dice

class player():
   def __init__(self, name, diceInHand, Brains, ShotGuns, typesOfDice):
      self.name = name
      self.numberOfDice = 3
      self.diceInHand = diceInHand
      self.Brains = Brains
      self.ShotGuns = ShotGuns
      self.typesOfDice = typesOfDice

   def getUsableDice(self):
      return self.diceInHand

   #User should have three dice they are using is their selection isn't full add that many more dice into the bag
   def selectDice(self, bagOfDice):
      if len(self.diceInHand) < self.numberOfDice:
         numberOfDiceNeeded = self.numberOfDice - len(self.diceInHand)
         for i in range(numberOfDiceNeeded):
            random.shuffle(bagOfDice)              #shuffle the bag of dice
            if len(bagOfDice) == 0:
               bagOfDice = dice.loadDiceBag(self.typesOfDice) #load the initial bag the users will pull from
            self.diceInHand.append(bagOfDice[0])   #pull a die from the bag and give it to users array diceInHand
            bagOfDice.pop()                        #remove that same die from the bagOfDice
      return self.diceInHand

   def refillDice(self, bagOfDice):
      self.diceInHand = self.selectDice(bagOfDice)
      print("You now have")
      for die in self.diceInHand:
         print(die.showColor())
      return self.diceInHand

   def UsersNextRoll(self, tempHolder): #Roll dice per user request
      print("You Rolled")
      nextRoll = roll(self.diceInHand)
      self.ShotGuns, tempHolder, rolls = nextRoll.rollDice(self.ShotGuns,tempHolder)#######################################################This needs to have the self.brains for checks on expansions rules
      return self.ShotGuns, tempHolder, rolls

   def userTurn(self, bagOfDice):
      _ = system('cls')
      startingValue = []

      print("player", self.name,"You have", len(self.Brains), "Brains and", len(self.ShotGuns), "ShotGuns ")

      while len(self.ShotGuns) <= 2:
         print("player", self.name,"You rolled", len(startingValue), "Brains and", len(self.ShotGuns), "ShotGuns ")
         decision = input("do you wish to roll again? y/n ")
         if decision == "y":
            _ = system('cls')
            self.diceInHand = self.refillDice(bagOfDice)
            self.ShotGuns, startingValue, rolls = self.UsersNextRoll(startingValue)
         if decision == "n":
            for staringBrain in startingValue: 
               self.Brains.append(staringBrain)
            break
      if len(self.ShotGuns) >= 3:
         self.brains = startingValue
         input("wa wa waaaaaaa you were shot too many times!")
      self.ShotGuns = []