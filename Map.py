import pygame
import Constants

import Units
import random
import time


# main graphics function
def display():
    # background, shouldn't be visible
    pygame.draw.rect(Constants.game_display, Constants.blue,
                     (Constants.FRAME_WIDTH, 0, Constants.FRAME_WIDTH,
                      Constants.FRAME_HEIGHT), 0)
    # draw map
    for y in range(20):
        for x in range(40):
            draw_map(x, y)


# can change the world map
def change_map(x, y, new_letter):
    global map_tile_contents
    map_tile_contents[x][y].tile_letter = new_letter
    map_tile_contents[x][y].get_tile_colour()


class Tile:
    def __init__(self, x, y, tile_letter):
        self.x = x
        self.y = y
        self.x_pos = (x * Constants.BLOCK_WIDTH)
        self.y_pos = (y * Constants.BLOCK_HEIGHT)

        self.tile_letter = tile_letter

        self.sand = 0
        self.max = 20

        self.tile_colour = (255, 0, 255)
        self.lighter_colour = (255, 0, 255)

    # uses the letters of map.txt to color the map
    def get_tile_colour(self):
        if self.tile_letter == "x":
            self.tile_colour = Constants.alt_blue
        if self.tile_letter == "s":
            self.tile_colour = Constants.orange
        if self.tile_letter == "-":
            self.tile_colour = Constants.blue

        # get lighter colour
        lighter = []  # temp list to store colour in

        # loop through r, g, b and make each a bit lighter
        for colour in self.tile_colour:
            # small change of different colour
            colour = min(255, colour + 30)
            lighter.append(colour)

        self.lighter_colour = tuple(lighter)


# draws a rectangle for every tile
def draw_map(x, y):
    global map_tile_contents

    # loop through the map tile contents (replace with something better?)
    tile_colour = map_tile_contents[x][y].tile_colour
    lighter_colour = map_tile_contents[x][y].lighter_colour

    x_pos = map_tile_contents[x][y].x_pos
    y_pos = map_tile_contents[x][y].y_pos

    # draw darker square first
    block1 = pygame.Rect(x_pos, y_pos,
                         Constants.BLOCK_WIDTH,
                         Constants.BLOCK_HEIGHT)
    pygame.draw.rect(Constants.game_display, tile_colour, block1)

    # draw lighter square on top
    block2 = pygame.Rect(x_pos + 1, y_pos + 1,
                         Constants.BLOCK_WIDTH - 2,
                         Constants.BLOCK_HEIGHT - 2)
    pygame.draw.rect(Constants.game_display, lighter_colour, block2)

    # draw darker square on top
    block3 = pygame.Rect(x_pos + 3, y_pos + 3,
                         Constants.BLOCK_WIDTH - 6,
                         Constants.BLOCK_HEIGHT - 6)
    pygame.draw.rect(Constants.game_display, tile_colour, block3)


# read map
def read_map(map_file):
    try:
        with open(map_file, 'r') as f:
            world_map = f.readlines()
        # removes /n new line bit
        world_map = [line.strip() for line in world_map]

        # create the initial map
        initialise_map(world_map)

    except OSError:
        print("Exit - Can't find map file: map.txt.")
        quit()


# initialise the map
def initialise_map(world_map):
    global map_tile_contents

    # loop through the map
    for y_grid, tile in enumerate(world_map):
        for x_grid, tile_contents in enumerate(tile):
            # if sand, add 20 sand to the tile
            if tile_contents == "s":
                map_tile_contents[x_grid][y_grid].sand = 20

            # add the tile contents
            map_tile_contents[x_grid][y_grid].tile_letter = tile_contents

            # set tile colour
            map_tile_contents[x_grid][y_grid].get_tile_colour()


# create a list of tiles to populate
rows, cols = (20, 40)
map_tile_contents = [[Tile(j, i, "x") for i in range(rows)] for j in range(cols)]






