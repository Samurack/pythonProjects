###############################################################################################
# https://pypi.org/project/browserhistory/
# http://buildandteach.com/wp-content/uploads/2019/03/Screen-Shot-2019-03-17-at-8.24.07-PM.png
# https://docs.python.org/3/tutorial/classes.html
###############################################################################################
class CollegeClass(): 
   def __init__(self, CollegeName, CollegeCost):
      self.CollegeName = CollegeName
      self.CollegeCost = CollegeCost

   def setCollegeInformation(self):
      vals = (self.CollegeName, self.CollegeCost)
      return vals

   def printCollegeInformation(self):
      print(self.CollegeName + ", " + self.CollegeCost)

   def printCollegeName(self):
      print(self.CollegeName)

   def printCollegeCost(self):
      print(self.CollegeCost)

   def getCollegeName(self):
      val = self.CollegeName
      return val

   def getCollegeCost(self):
      val = self.CollegeCost
      return val