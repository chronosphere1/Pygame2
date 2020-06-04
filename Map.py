import pygame
import Constants

import Units
import random
import time


# main graphics function
def display():
    global world_map

    # background, shouldn't be visible
    pygame.draw.rect(Constants.game_display, Constants.blue,
                     (Constants.FRAME_WIDTH, 0, Constants.FRAME_WIDTH,
                      Constants.FRAME_HEIGHT), 0)
    # draw map
    draw_map(world_map)


# can change the world map
def change_map(x, y, new_letter):
    global world_map

    # create a new list to put the new map contents in
    rows, cols = (20, 40)
    new_map = [[0 for i in range(cols)] for j in range(rows)]

    # loop through the map, change when conditions are met
    for y_grid, tile in enumerate(world_map):
        for x_grid, tile_contents in enumerate(tile):
            if x_grid == x and y_grid == y:
                new_map[y_grid][x_grid] = new_letter
            else:
                new_map[y_grid][x_grid] = tile_contents

    world_map = new_map


class Tile:
    def __init__(self, x, y):
        self.tile_colour = (255, 0, 255)
        self.lighter_colour = (255, 0, 255)
        self.x = x
        self.y = y
        self.sand = 20
        self.max = 20

    # uses the letters of map.txt to color the map
    def get_tile_colour(self, tile_contents):
        self.tile_colour = Constants.black
        if tile_contents == "x":
            self.tile_colour = Constants.alt_blue
        if tile_contents == "s":
            self.tile_colour = Constants.orange
        if tile_contents == "-":
            self.tile_colour = Constants.blue

        return self.tile_colour

    def get_alt_tile_colour(self, tile_colour):
        # get lighter colour
        lighter = []

        # loop through r, g, b and make each a bit lighter
        for colour in tile_colour:
            # small change of different colour
            colour = min(255, colour + 30)
            lighter.append(colour)

        self.lighter_colour = tuple(lighter)
        return self.lighter_colour


# draws a rectangle for every letter in map.txt
def draw_map(map_tiles):
    # loop through the map
    for y_grid, tile in enumerate(map_tiles):
        for x_grid, tile_contents in enumerate(tile):
            # print("{},{}: {}".format(x_grid, y_grid, tile_contents))
            x_pos = (x_grid * Constants.BLOCK_WIDTH)
            y_pos = (y_grid * Constants.BLOCK_HEIGHT)

            # create the tile contents
            individual_tile = Tile(x_grid, y_grid)

            # get tile colours
            tile_colour = individual_tile.get_tile_colour(tile_contents)
            lighter_colour = individual_tile.get_alt_tile_colour(tile_colour)

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
    global world_map
    try:
        with open(map_file, 'r') as f:
            world_map = f.readlines()
        # removes /n new line bit
        world_map = [line.strip() for line in world_map]
        return world_map

    except OSError:
        print("Exit - Can't find map file: map.txt.")
        quit()


# initialised the map
def initialise_map(map_tiles):
    # loop through the map
    for y_grid, tile in enumerate(map_tiles):
        for x_grid, tile_contents in enumerate(tile):
            x_pos = (x_grid * Constants.BLOCK_WIDTH)
            y_pos = (y_grid * Constants.BLOCK_HEIGHT)

            # create the tile contents
            individual_tile = Tile(x_grid, y_grid)


world_map = read_map(Constants.map_file)