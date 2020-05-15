import pygame
import Constants
import Buildings

FRAME_WIDTH = Constants.DISPLAY_WIDTH / 2  # currently 600
FRAME_HEIGHT = Constants.DISPLAY_HEIGHT / 2  # currently 400
BLOCK_WIDTH = Constants.DISPLAY_WIDTH / 20
BLOCK_HEIGHT = Constants.DISPLAY_HEIGHT / 20


# main graphics function
def display(world_map):
    # background, shouldn't be visible
    pygame.draw.rect(Constants.game_display, Constants.blue, (FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT), 0)
    # draw map
    draw_map(world_map)
    # grid
    grid()


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


# draws a rectangle for every letter in map.txt
def draw_map(map_tiles):
    # loop through the map
    for j, tile in enumerate(map_tiles):
        for i, tile_contents in enumerate(tile):
            # print("{},{}: {}".format(i, j, tile_contents))
            block = pygame.Rect(i * BLOCK_WIDTH + FRAME_WIDTH,  # start offset by frame width
                                j * BLOCK_HEIGHT,
                                BLOCK_WIDTH,
                                BLOCK_HEIGHT)
            pygame.draw.rect(Constants.game_display, get_tile_colour(tile_contents), block)


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


# draw a grid on top
def grid():
    for x in range(0, 10):
        # vertical line starting top middle, each iteration 10% further to east
        vertical_start_line = [FRAME_WIDTH + FRAME_WIDTH / 10 * x, 0]
        vertical_end_line = [FRAME_WIDTH + FRAME_WIDTH / 10 * x, FRAME_HEIGHT]
        # horizontal line starting top middle, each iteration 10% further to south
        horizontal_start_line = [FRAME_WIDTH, FRAME_HEIGHT / 10 * x]
        horizontal_end_line = [FRAME_WIDTH * 2, FRAME_HEIGHT / 10 * x]

        pygame.draw.line(Constants.game_display,
                         Constants.black,
                         vertical_start_line,
                         vertical_end_line,
                         1)

        pygame.draw.line(Constants.game_display,
                         Constants.black,
                         horizontal_start_line,
                         horizontal_end_line,
                         1)
















