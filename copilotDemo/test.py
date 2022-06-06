#draw ironman in python
import turtle
import math
import random
import time
import os

def draw_ironman(t, length, angle):
    """Draw a square with turtle t, of side length length, at angle angle"""
    for i in range(4):
        t.forward(length)
        t.right(angle)
draw_ironman(turtle, 100, 90)