import pgzrun
from random import randint
import pygame

WIDTH = 800
HEIGHT = 600

clock = pygame.time.Clock()

merchant = Actor("merchant/mercant_idle_1")
merchant.pos = 400, 545

trash_monster = Actor("trash_monster/trash_monster_idle1")
trash_monster.pos = 0, 545

moon = Actor("dungeon_ruins_tileset/moon")
moon.pos = 800, 200

clouds = Actor("dungeon_ruins_tileset/clouds")
clouds.pos = randint(800, 1000), randint(10, 200)

arch1 = Actor("dungeon_ruins_tileset/arch1")
arch1.pos = randint(700, 1900), 514

arch2 = Actor("dungeon_ruins_tileset/arch2")
arch2.pos = randint(800, 3000), 514

arch3 = Actor("dungeon_ruins_tileset/arch3")
arch3.pos = randint(900, 1200), 530

beam1 = Actor("dungeon_ruins_tileset/beam1")
beam1.pos = randint(100, 800), 514

beam2 = Actor("dungeon_ruins_tileset/beam2")
beam2.pos = randint(1100, 1600), 514

beam3 = Actor("dungeon_ruins_tileset/beam3")
beam3.pos = randint(120, 900), 548

beam4 = Actor("dungeon_ruins_tileset/beam4")
beam4.pos = randint(1300, 1400), 549

box1 = Actor("dungeon_ruins_tileset/box1")
box1.pos = randint(400, 1800), 514

box2 = Actor("dungeon_ruins_tileset/box2")
box2.pos = randint(500, 3200), 514

box3 = Actor("dungeon_ruins_tileset/box3")
box3.pos = randint(800, 1900), 530

box4 = Actor("dungeon_ruins_tileset/box4")
box4.pos = randint(700, 2000), 530

bush1 = Actor("dungeon_ruins_tileset/bush1")
bush1.pos = randint(800, 1800), 538

bush2 = Actor("dungeon_ruins_tileset/bush2")
bush2.pos = randint(900, 1200), 553

leaningcrosses1 = Actor("dungeon_ruins_tileset/leaningcrosses1")
leaningcrosses1.pos = randint(800, 2000), 540

leaningcrosses2 = Actor("dungeon_ruins_tileset/leaningcrosses2")
leaningcrosses2.pos = randint(600, 2100), 525

fence = Actor("dungeon_ruins_tileset/fence")
fence.pos = randint(220, 900), 554

grass = Actor("dungeon_ruins_tileset/grass")
grass.pos = randint(230, 3000), 556

construct1 = Actor("dungeon_ruins_tileset/construct1")
construct1.pos = randint(400, 2500), 515

construct2 = Actor("dungeon_ruins_tileset/construct2")
construct2.pos = randint(200, 1600), 515

construct3 = Actor("dungeon_ruins_tileset/construct3")
construct3.pos = randint(200, 1800), 509

background_actors_list = []
background_actors_list.append(arch3)
background_actors_list.append(box3)
background_actors_list.append(clouds)
background_actors_list.append(arch1)
background_actors_list.append(leaningcrosses1)
background_actors_list.append(beam2)
background_actors_list.append(beam1)
background_actors_list.append(leaningcrosses2)
background_actors_list.append(beam4)
background_actors_list.append(box1)
background_actors_list.append(beam3)
background_actors_list.append(box4)
background_actors_list.append(bush1)
background_actors_list.append(construct2)
background_actors_list.append(bush2)
background_actors_list.append(fence)
background_actors_list.append(grass)
background_actors_list.append(box2)
background_actors_list.append(construct1)
background_actors_list.append(arch2)
background_actors_list.append(construct3)

background_images = []
background_images.append('background1')
background_images.append('background1')
background_images.append('background1')
background_images.append('background2')
background_images.append('background2')
background_images.append('background2')
background_images.append('background3')
background_images.append('background3')
background_images.append('background3')


background_images_index = 0

merchant_idle_moves = []
merchant_idle_moves.append('merchant/mercant_run_1')
merchant_idle_moves.append('merchant/mercant_run_2')
merchant_idle_moves.append('merchant/mercant_run_3')
merchant_idle_moves.append('merchant/mercant_run_4')
merchant_idle_moves.append('merchant/mercant_run_5')

merchant_idle_index = 0

trash_monster_moves = []
trash_monster_moves.append('trash_monster/trash_monster_run1')
trash_monster_moves.append('trash_monster/trash_monster_run2')
trash_monster_moves.append('trash_monster/trash_monster_run3')
trash_monster_moves.append('trash_monster/trash_monster_run4')
trash_monster_moves.append('trash_monster/trash_monster_run5')
trash_monster_moves.append('trash_monster/trash_monster_run6')

trash_monster_index = 0

trash_monster_kill_moves = []
trash_monster_kill_moves.append('trash_monster/trash_monster_kill1')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill1')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill2')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill2')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill3')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill3')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill4')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill4')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill5')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill5')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill6')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill6')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill7')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill7')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill8')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill8')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill9')
trash_monster_kill_moves.append('trash_monster/trash_monster_kill9')

trash_monster_kill_index = 0

trash_monster_idle_moves = []
trash_monster_idle_moves.append('trash_monster/trash_monster_idle1')
trash_monster_idle_moves.append('trash_monster/trash_monster_idle1')
trash_monster_idle_moves.append('trash_monster/trash_monster_idle3')
trash_monster_idle_moves.append('trash_monster/trash_monster_idle3')
trash_monster_idle_moves.append('trash_monster/trash_monster_idle4')
trash_monster_idle_moves.append('trash_monster/trash_monster_idle4')
trash_monster_idle_moves.append('trash_monster/trash_monster_idle5')
trash_monster_idle_moves.append('trash_monster/trash_monster_idle5')
trash_monster_idle_moves.append('trash_monster/trash_monster_idle6')
trash_monster_idle_moves.append('trash_monster/trash_monster_idle6')

trash_monster_idle_index = 0

trash_monster_forward = True
forward = False
game_over = False
kill_move = False
monster_idle = False
score = 0
number_of_updates = 0

scores = []

def update_high_scores():
	global score, scores
	filename = r"D:\code\Python_desktop_application\python-games\zombie-runner\high-scores.txt"
	scores = []
	with open(filename, "r") as file:
		line = file.readline()
		high_scores = line.split()
		for high_score in high_scores:
			if(score > int(high_score)):
				scores.append(str(score) + " ")
				score = int(high_score)
			else:
				scores.append(str(high_score) + " ")
	with open(filename, "w") as file:
		for high_score in scores:
			file.write(high_score)

def display_high_scores():
	screen.draw.text("HIGH SCORES", (350, 150), color="black")
	y = 175
	position = 1
	for high_score in scores:
		screen.draw.text(str(position) + ". " + high_score, (350, y), color="black")
		y += 25
		position += 1

def draw():
	global background_images_index, background_images, background_actors_list

	if not monster_idle:
		if background_images_index >= 8:
			background_images_index = 0
		else:	
			background_images_index += 1

		screen.blit(background_images[background_images_index], (0, 0))
		for actor in background_actors_list:
			actor.draw()
		moon.draw()	
		merchant.draw()
		trash_monster.draw()
		screen.draw.text("Score: " + str(score), (700, 5), color="black")
	else:
		screen.blit(background_images[background_images_index], (0, 0))
		for actor in background_actors_list:
			actor.draw()
		moon.draw()	
		trash_monster.draw()
		display_high_scores()

def on_key_up(key):
	global forward

	if key == keys.RIGHT:
		forward = True
		if merchant.x < 755:
			merchant.x += 5
		else:
			merchant.x += 0
		if trash_monster.x > 0:
			trash_monster.x -= 6

	if key == keys.LEFT:
		forward = True
		if merchant.x < 755:
			merchant.x += 5
		else:
			merchant.x += 0
		if trash_monster.x > 0:
			trash_monster.x -= 6
	forward = False


def idleMove():
	global trash_monster_idle_moves, trash_monster_idle_index
	if trash_monster_idle_index >= len(trash_monster_idle_moves):
		trash_monster_idle_index = 0
	trash_monster.image = trash_monster_idle_moves[trash_monster_idle_index]
	trash_monster_idle_index += 1

def killMove(): ##################################################################Add merchent death sequence to this method
	global trash_monster_kill_moves, trash_monster_kill_index, monster_idle
	if trash_monster_kill_index >= len(trash_monster_kill_moves):
		monster_idle = True
	else:
		trash_monster.image = trash_monster_kill_moves[trash_monster_kill_index]
		trash_monster_kill_index += 1

def update():
	global kill_move, score, number_of_updates, merchant_idle_index, merchant_idle_moves
	global trash_monster_index, trash_monster_moves, trash_monster_kill_index
	clock.tick(10)

	if not kill_move:
		if merchant_idle_index >= len(merchant_idle_moves):
			merchant_idle_index = 0

		merchant.image = merchant_idle_moves[merchant_idle_index]
		merchant_idle_index += 1

		if trash_monster_index >= len(trash_monster_moves):
			trash_monster_index = 0

		trash_monster.image = trash_monster_moves[trash_monster_index]
		trash_monster_index += 1
		if not forward:
			merchant.x -= 1
		if trash_monster.x < 720:
			trash_monster.x += 4
			if number_of_updates == 90:
				number_of_updates = 0
				score += 1
			else:
				number_of_updates += 1


		if merchant.collidepoint(trash_monster.x, trash_monster.y):
			kill_move = True
			update_high_scores()
	else:
		if not monster_idle:
			killMove()
		else:
			idleMove()
	if not kill_move:
		for actor in background_actors_list:
			if actor.right > 0:
				actor.x -= 4
			else:
				actor.x = randint(800, 3000)
		if moon.right > 0:
			moon.x -= 0.4
		else:
			moon.x = randint(800, 3000)
pgzrun.go()