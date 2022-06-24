# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
#1. Convert radians into degrees
# Write a function in Python that accepts one numeric parameter.
# This parameter will be the measure of an angle in radians. 
# The function should convert the radians into degrees and then return that value.
# While you might find a Python library to do this for you, you should write the function yourself. 
# One hint you get is that you'll need to use Pi in order to solve this problem. 
# You can import the value for Pi from Python's math module.

import math
import sys

def convertToDegrees():
    userNumber = int(input("What Radian would you like to convert? "))
    result = userNumber * 180/math.pi
    print("Mine Result", result)
    print("Program Result", math.degrees(userNumber))

convertToDegrees()