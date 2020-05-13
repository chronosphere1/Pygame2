import pygame

# set resolution
display_width = 1200
display_height = 800

# set resolution
game_display = pygame.display.set_mode((display_width, display_height))

# window title
pygame.display.set_caption('pygame2')
# game clock
clock = pygame.time.Clock()

#  sizes
width_20_percent = int(display_width / 5)
height_10_percent = int(display_height / 10)

# RBG colours
black = (0, 0, 0)
red = (255, 0, 0)
grey = (195, 195, 195)
white = (255, 255, 255)