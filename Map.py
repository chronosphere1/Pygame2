import pygame
import Constants
import Textbox

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
    map_tile_contents[x][y].change_tile_letter(new_letter)


def map_colour_changer(x, y):
    map_tile_contents[x][y].super_light()



class Tile:
    def __init__(self, x, y, tile_letter):
        self.x = x
        self.y = y
        self.x_pos = (x * Constants.BLOCK_WIDTH)
        self.y_pos = (y * Constants.BLOCK_HEIGHT)

        self.tile_letter = tile_letter

        self.sand = 0
        self.water = 0

        self.max = 20

        self.tile_colour = (255, 0, 255)
        self.lighter_colour = (255, 0, 255)
        self.super_light_colour = (255, 0, 255)

    # uses the letters of map.txt to color the map
    def get_tile_colour(self):
        if self.tile_letter == "x":
            self.tile_colour = Constants.alt_blue
        elif self.tile_letter == "s":
            self.tile_colour = Constants.orange
        elif self.tile_letter == "-":
            self.tile_colour = Constants.blue
        elif self.tile_letter == "r":
            self.tile_colour = Constants.alt_brown

        # get lighter colour
        lighter = []  # temp list to store colour in
        lighter2 = []

        # loop through r, g, b and make each a bit lighter
        for colour in self.tile_colour:
            # small change of different colour
            random_addition = random.randint(0, 30)
            colour = min(255, colour + 30)
            colour2 = min(255, colour + random_addition )
            lighter.append(colour)
            lighter2.append(colour2)

        self.lighter_colour = tuple(lighter)
        self.super_light_colour = tuple(lighter2)

    def super_light(self):
        self.lighter_colour = self.super_light_colour

    def change_tile_letter(self, new_tile):
        self.tile_letter = new_tile
        self.get_tile_colour()

    def dig_sand(self):
        self.sand -= 1
        if self.sand == 0:
            Textbox.textbox.add_message(f"Under the sand you find rock")
            self.change_tile_letter("r")
        return True

    def dig_shallow_water(self):
        self.water -= 1
        if self.water == 0:
            Textbox.textbox.add_message(f"Under the water you find sand")
            self.change_tile_letter("s")
            self.sand = 20


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
    pygame.draw.rect(Constants.game_display, tile_colour, block1, 2)

    # draw lighter square on top
    block2 = pygame.Rect(x_pos + 1, y_pos + 1,
                         Constants.BLOCK_WIDTH - 2,
                         Constants.BLOCK_HEIGHT - 2)
    pygame.draw.rect(Constants.game_display, lighter_colour, block2)
    #
    # # draw darker square on top
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
                map_tile_contents[x_grid][y_grid].sand = 10
            elif tile_contents == "-":
                map_tile_contents[x_grid][y_grid].water = 10

            # add the tile contents
            map_tile_contents[x_grid][y_grid].change_tile_letter(tile_contents)


class Changer:
    def __init__(self):
        self.x = 20
        self.y = 10

    def change(self, x, y):
        self.x = x
        self.y = y

        if self.x < 39:
            map_colour_changer(self.x + 1, self.y + 0)
        if self.y < 19:
            map_colour_changer(self.x + 0, self.y + 1)
        if self.x > 0:
            map_colour_changer(self.x - 1, self.y + 0)
        if self.y > 0:
            map_colour_changer(self.x - 0, self.y - 1)

        map_colour_changer(self.x, self.y)


# create a list of tiles to populate
rows, cols = (20, 40)
map_tile_contents = [[Tile(j, i, "x") for i in range(rows)] for j in range(cols)]

# load map changer
change = Changer()

