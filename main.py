# modules
import pygame
from pygame.locals import *
from pygame import *
import sys
init()


# screen variables
screen_width, screen_height = 900, 650
screen = display.set_mode((screen_width, screen_height))
# screen title
display.set_caption('Base')
# screen icon
screen_icon = image.load('graphics/icon/icon.png')
display.set_icon(screen_icon)


# ticks
clock = time.Clock()


# colors
GREY = (60, 60, 60)
WHITE = (255, 255, 255)
# background color
BG = GREY


def draw_all_objects():
	# background
	screen.fill(BG)


# main while
while True:
	# keyboard
	keys = key.get_pressed()
	# mouse
	mouse_pressed = mouse.get_pressed()
	mouse_click = MOUSEBUTTONDOWN
	# mouse coordinates
	mouse_x = mouse.get_pos()[0]
	mouse_y = mouse.get_pos()[1]

	# keys check
	for event in pygame.event.get():
		# quit
		if event.type == QUIT:
			quit()
			sys.exit()

	# functions
	draw_all_objects()

	# display update
	display.flip()
	clock.tick(60)