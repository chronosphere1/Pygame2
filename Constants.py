import pygame

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
WIDTH_20_PERCENT = int(DISPLAY_WIDTH / 5)
HEIGHT_10_PERCENT = int(DISPLAY_HEIGHT / 10)

# RBG colours
black = (0, 0, 0)
red = (255, 0, 0)
grey = (195, 195, 195)
white = (255, 255, 255)
blue = (62, 103, 206)
alt_blue = (62, 67, 206)
dark_blue = (31, 52, 103)
orange = (255, 189, 51)
brown = (103, 87, 31)

# map file
map_file = "map.txt"
square_building = "building1.bmp"