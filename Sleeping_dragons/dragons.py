import math
from lair import Easy_Lair, Medium_Lair, Hard_Lair
from pgzero.builtins import Actor, animate, keyboard

"""These constants define the size of the game window, and its center"""
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)

"""Sets font color to black"""
FONT_COLOR = (0, 0, 0) 

"""This sets the number of eggs needed to win the game"""
EGG_TARGET = 20

"""This sets the hero's position at the start of the game"""
HERO_START = (200, 300)

"""This is the distance in pixels at which the dragon can attack the hero"""
ATTACK_DISTANCE = 200

"""This is the number of seconds the dragonsm stay awake"""
DRAGON_WAKE_TIME = 2

"""This sets the number of seconds the eggs are hidden"""
EGG_HIDE_TIME = 2

"""This sets the number of pixels the hero moves by with each key press"""
MOVE_DISTANCE = 5

lives = 3
eggs_collected  = 0 
game_over = False
game_complete = False
reset_required = False

lairs = [Easy_Lair(), Medium_Lair(), Hard_Lair()]
hero = Actor("hero", pos=HERO_START)

def draw():
	"""Draw the screen, with the dragons, hero, eggs, egg counter, and lives counter
	"""
	global lairs, eggs_collected, lives, game_complete
	screen.clear()
	screen.blit("dungeon", (0, 0)) #Adds background to game

	if game_over:
		screen.draw.text("GAME OVER!", fontsize=60, center=CENTER, color=FONT_COLOR)
	elif game_complete:
		screen.draw.text("YOU WON!", fontsize=60, center=CENTER, color=FONT_COLOR)
	else:
		hero.draw()
		draw_lairs(lairs)
		draw_counters(eggs_collected, lives)

def draw_lairs(lairs_to_draw: list[str, str, str]):
	"""Draw the dragons and the eggs

	Args:
		lairs_to_draw (list[str, str, str]): a list of each lair
	"""
	for lair in lairs_to_draw:
		lair.dragon.draw()
		if lair.egg_hidden is False:
			lair.eggs.draw()

def draw_counters(eggs_collected: int , lives: int):
	"""Draw the life, and egg totals

	Parameters
	----------
	eggs_collected : int
		number of eggs the user has collected
	lives : int
		number of lives the user has
	"""
	screen.blit("egg-count", (0, HEIGHT - 30))
	screen.draw.text(str(eggs_collected),
					 fontsize=40,
					 pos=(30, HEIGHT - 30),
					 color=FONT_COLOR)
	screen.blit("life-count", (60, HEIGHT - 30))
	screen.draw.text(str(lives),
					 fontsize=40,
					 pos=(90, HEIGHT - 30),
					 color=FONT_COLOR)

def update():
	"""Get keyboard strokes for users moves
	"""
	if keyboard.right:
		hero.x += MOVE_DISTANCE
		if hero.x > WIDTH:
			hero.x = WIDTH
	elif keyboard.left:
		hero.x -= MOVE_DISTANCE
		if hero.x < 0:
			hero.x = 0
	elif keyboard.down:
		hero.y += MOVE_DISTANCE
		if hero.y > HEIGHT:
			hero.y = HEIGHT
	elif keyboard.up:
		hero.y -= MOVE_DISTANCE
		if hero.y < 0:
			hero.y = 0
	check_for_collision()

def update_lairs():
	"""Update the dragons so they will either be awake or asleep at the right times
	"""
	global lairs, hero, lives
	for lair in lairs:
		if lair.dragon.image == "dragon-asleep":
			update_sleeping_dragon(lair)
		elif lair.dragon.image == "dragon-awake":
			update_waking_dragon(lair)
		update_egg(lair)

"""This function schedules a call to another function at regular intervals. 1 is the number of seconds between function calls"""
clock.schedule_interval(update_lairs, 1)

def update_sleeping_dragon(lair: str):
	"""Update the sleeping dragons timer

	Parameters
	----------
	lair : str
		Which lair is this dragon is in
	"""
	if lair.sleep_counter >= lair.sleep_length:
		lair.dragon.image = "dragon-awake"
		lair.sleep_counter = 0
	else:
		lair.sleep_counter += 1

def	update_waking_dragon(lair: str):
	"""Update the waking dragons time

	Parameters
	----------
	lair : str
		Which lair is this dragon is in? 😲
	"""
	if lair.wake_counter >= DRAGON_WAKE_TIME:
		lair.dragon.image = "dragon-asleep"
		lair.wake_counter = 0
	else:
		lair.wake_counter += 1


def update_egg(lair: str):
	"""Add more eggs as the user collects them

	Parameters
	----------
	lair : str
		Which lair is the egg in?  🥚
	"""
	if lair.egg_hidden is True:
		if lair.egg_hide_counter >= EGG_HIDE_TIME:
			lair.egg_hidden = False
			lair.egg_hide_counter = 0
		else:
			lair.egg_hide_counter += 1

def check_for_collision():
	"""Check to see if the user is within range of either the egg, or the dragon
	"""
	global lairs, eggs_collected, lives, reset_required, game_complete
	for lair in lairs:
		if lair.egg_hidden is False:
			check_for_egg_collision(lair)
		if lair.dragon.image == "dragon-awake" and reset_required is False:
			check_for_dragon_collision(lair)

def check_for_dragon_collision(lair: str):
	"""Is the user within reach of a dragon? 

	Parameters
	----------
	lair : str
		Which lair is this dragon is in? 😲
	"""
	x_distance = hero.x - lair.dragon.x
	y_distance = hero.y - lair.dragon.y
	distance = math.hypot(x_distance, y_distance)
	if distance < ATTACK_DISTANCE:
		handle_dragon_collision()

def handle_dragon_collision():
	"""If the user is within reach of the dragon BURN THEM! 🔥
	"""
	global reset_required
	reset_required = True
	animate(hero, pos=HERO_START, on_finished=subtract_life)

def check_for_egg_collision(lair: str):
	"""Check if the user is within reach of an egg

	Parameters
	----------
	lair : str
		which lair are we in? 🚪
	"""
	global eggs_collected, game_complete
	if hero.colliderect(lair.eggs):
		lair.egg_hidden = True
		eggs_collected += lair.egg_count
		if eggs_collected >= EGG_TARGET:
			game_complete = True

def subtract_life():
	"""Remove a heart from the user
	"""
	global lives, reset_required, game_over
	lives -= 1
	if lives == 0:
		game_over = True
	reset_required = False