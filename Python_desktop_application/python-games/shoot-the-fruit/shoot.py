import pgzrun
from random import randint

apple = Actor("apple")
pear = Actor("pear")
score = 0
produce_pear = 2

def draw():
	global produce_pear
	screen.clear()
	if produce_pear == 3:
		pear.draw()
	else:	
		apple.draw()

def place_fruit(Actor):
	Actor.x = randint(10, 800)
	Actor.y = randint(10, 600)

def on_mouse_down(pos):
	global score
	global produce_pear
	if produce_pear == 3:
		if not pear.collidepoint(pos):
			print("Good Catch!")
			place_fruit(apple)
		else:
			print("You Hit the Pear!")
			print("Your Score was ", score)
			score = 0
			place_fruit(pear)
	elif apple.collidepoint(pos):
		print("Good Shot!")
		place_fruit(apple)
		score += 1
	else:
		print("You Missed!")
		print("Your Score was ", score)
		score = 0
		#quit()
	produce_pear = randint(0, 5)

pgzrun.go()
