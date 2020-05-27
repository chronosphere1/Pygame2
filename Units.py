import pygame
import Constants
import Map
import Randoms

local_map = []


class Unit:
    def __init__(self, name, image_location, x, y):
        self.name = name
        self.amount = 1
        self.x = x
        self.y = y

        self.colour = (255, 0, 255)

        # loads the image
        self.img = pygame.image.load(image_location)
        # creates a rectangle of the image size
        self.rect = self.img.get_rect().size

    # draw the player
    def draw_player(self, frame):
        # every few frames, change the colour

        self.colour = Randoms.random_colour_generator2(frame)

        lighter = []

        for colour in self.colour:
            colour = min(255, colour + 50)
            lighter.append(colour)

        lighter_colour = tuple(lighter)

        # draw a 20x20 circle with mad colours
        pygame.draw.ellipse(Constants.game_display, Constants.black, [self.x, self.y, 20, 20])
        pygame.draw.ellipse(Constants.game_display, self.colour, [self.x + 1, self.y + 1, 18, 18])
        # lighter inner circle
        pygame.draw.ellipse(Constants.game_display, lighter_colour, [self.x + 5, self.y + 5, 10, 10])


# draws the player on the grid
def make_player(frame):
    player.draw_player(frame)


def place_building(building_name):
    if building_name == "Pump":
        print("Lets make a pump")


def map_contents(full_map):
    global local_map
    local_map = full_map


# player hits x button
def x_action():
    global local_map
    # Current X plus half of the width of the player size, divided by block height
    # this puts the 'location' at the center of the player image
    map_x = (player.x + player.rect[0] / 2) / Constants.BLOCK_HEIGHT
    map_y = (player.y + player.rect[0] / 2) / Constants.BLOCK_WIDTH

    # determine how far the player is from the grid border
    x_border = map_x - int(map_x)
    y_border = map_y - int(map_y)

    # convert to a grid number by removing decimals
    grid_x = int(map_x)
    grid_y = int(map_y)

    # what's on the map?
    tile_terrain = local_map[grid_x][grid_y]

    # if within 20% of the edge, ignore
    if x_border < 0.2 or x_border > 0.8\
            or y_border < 0.2 or y_border > 0.8:
        print("too close to the border")

    else:
        print("map location {},{}".format(grid_x, grid_y))
        if tile_terrain == "s":
            print("Standing on sand")


def check_grid_location(x_grid, y_grid):
    pass


player = Unit("Goku", Constants.player, x=300, y=300)
