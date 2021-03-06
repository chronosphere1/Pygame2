import pygame
import random
import numpy as np

# set resolution
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 800

# set resolution
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# window title
pygame.display.set_caption("Don't drown")
# game clock
clock = pygame.time.Clock()

#  sizes
WIDTH_5_PERCENT = int(DISPLAY_WIDTH / 20)
HEIGHT_5_PERCENT = int(DISPLAY_HEIGHT / 20)

WIDTH_10_PERCENT = int(DISPLAY_WIDTH / 10)
HEIGHT_10_PERCENT = int(DISPLAY_HEIGHT / 10)

HEIGHT_20_PERCENT = int(DISPLAY_HEIGHT / 5)
WIDTH_20_PERCENT = int(DISPLAY_WIDTH / 5)

FRAME_WIDTH = 1200
FRAME_HEIGHT = 600
BLOCK_WIDTH = 30
BLOCK_HEIGHT = 30


# RBG colours
black = (0, 0, 0)
red = (255, 0, 0)
grey = (195, 195, 195)
light_grey = (215, 215, 215)
white = (255, 255, 255)
blue = (62, 103, 206)
alt_blue = (62, 67, 206)
dark_blue = (31, 52, 103)
light_blue = (92, 97, 236)
orange = (255, 189, 51)
brown = (73, 56, 41)
light_brown = (129, 108, 91)
alt_brown = (169, 161, 140)

see_through_blue = (62, 103, 206, 200)
see_through_dark_blue = (31, 52, 103, 150)
see_through_white = (0, 0, 0, 150)


# font
def font(size):
    return pygame.font.SysFont('impact.ttf', size)


# map file
map_file = "map.txt"

# building
square_building = 'building1.bmp'
