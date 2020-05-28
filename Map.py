import pygame
import Constants
import Units
import random


# main graphics function
def display(world_map):
    # background, shouldn't be visible
    pygame.draw.rect(Constants.game_display, Constants.blue,
                     (Constants.FRAME_WIDTH, 0, Constants.FRAME_WIDTH,
                      Constants.FRAME_HEIGHT), 0)
    # draw map
    draw_map(world_map)


# uses the letters of map.txt to color the map
def get_tile_colour(tile_contents):
    tile_colour = Constants.black
    if tile_contents == "x":
        tile_colour = Constants.alt_blue
    if tile_contents == "s":
        tile_colour = Constants.orange
    if tile_contents == "-":
        tile_colour = Constants.blue

    return tile_colour


def get_alt_tile_colour(tile_colour):
    # get lighter colour
    lighter = []

    # loop through r, g, b and make each a bit lighter
    for colour in tile_colour:
        colour = min(255, colour + 20)
        lighter.append(colour)

    lighter_colour = tuple(lighter)
    return lighter_colour


# draws a rectangle for every letter in map.txt
def draw_map(map_tiles):
    # create a list to put the map contents in
    rows, cols = (20, 40)
    map_contents = [[0 for i in range(rows)] for j in range(cols)]

    # loop through the map
    for y_grid, tile in enumerate(map_tiles):
        for x_grid, tile_contents in enumerate(tile):
            # print("{},{}: {}".format(x_grid, y_grid, tile_contents))
            x_pos = (x_grid * Constants.BLOCK_WIDTH)
            y_pos = (y_grid * Constants.BLOCK_HEIGHT)

            # add to map contents
            map_contents[x_grid][y_grid] = tile_contents

            # get tile colours
            tile_colour = get_tile_colour(tile_contents)
            lighter_colour = get_alt_tile_colour(tile_colour)

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


    # send the map
    Units.map_contents(map_contents)


# read map
def read_map(map_file):
    try:
        with open(map_file, 'r') as f:
            world_map = f.readlines()
        # removes /n new line bit
        world_map = [line.strip() for line in world_map]
        return world_map

    except OSError:
        print("Exit - Can't find map file: map.txt.")
        quit()

# # draw a grid on top
# def grid():
#     for x in range(0, 20):
#         # vertical line starting top, each iteration 10% further to east
#         vertical_start_line = [Constants.FRAME_WIDTH / 20 * x, 0]
#         vertical_end_line = [Constants.FRAME_WIDTH / 20 * x, Constants.FRAME_HEIGHT]
#         # horizontal line starting top, each iteration 10% further to south
#         horizontal_start_line = [0, Constants.FRAME_WIDTH / 20 * x]
#         horizontal_end_line = [Constants.FRAME_WIDTH, Constants.FRAME_WIDTH / 20 * x]
#
#         pygame.draw.line(Constants.game_display,
#                          Constants.black,
#                          vertical_start_line,
#                          vertical_end_line,
#                          1)
#
#         pygame.draw.line(Constants.game_display,
#                          Constants.black,
#                          horizontal_start_line,
#                          horizontal_end_line,
#                          1)
