import pygame
import Constants
import Map
import Randoms
import Resources

local_map = []


class Unit:
    def __init__(self, name, x, y):
        self.name = name
        self.amount = 1
        self.x = x
        self.y = y
        self.x_border = 0.0
        self.y_border = 0.0
        self.map_x = 1
        self.map_y = 1

        self.colour = (255, 0, 255)

        # creates a rectangle of the player size
        self.rect = (20, 20)

    def update_grid_location(self):
        # Current X plus half of the width of the player size, divided by block height
        # this puts the 'location' at the center of the player image
        self.map_x = (self.x + player.rect[0] / 2) / Constants.BLOCK_HEIGHT
        self.map_y = (self.y + player.rect[0] / 2) / Constants.BLOCK_WIDTH

        # determine how far the player is from the grid border
        self.x_border = self.map_x - int(self.map_x)
        self.y_border = self.map_y - int(self.map_y)

        # get rid of decimal of grid location
        self.map_x = int(self.map_x)
        self.map_y = int(self.map_y)

    # draw the player
    def draw_player(self, frame):
        # every few frames, change the colour

        self.colour = Randoms.player_colour.slower(frame)

        lighter = []
        # get lighter colour
        for colour in self.colour:
            colour = min(255, colour + 50)
            lighter.append(colour)

        lighter_colour = tuple(lighter)

        # draw a 20x20 circle with mad colours
        pygame.draw.ellipse(Constants.game_display, Constants.black, [self.x, self.y, 20, 20])
        pygame.draw.ellipse(Constants.game_display, self.colour, [self.x + 1, self.y + 1, 18, 18])
        # lighter inner circle
        pygame.draw.ellipse(Constants.game_display, lighter_colour, [self.x + 5, self.y + 5, 10, 10])

    def player_tile(self, x, y):
        pass


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

    # what's on the map?
    tile_terrain = Map.map_tile_contents[player.map_x][player.map_y].tile_letter

    Resources.x_action(player.map_x, player.map_y, tile_terrain)


# create player
player = Unit("Goku", x=600, y=300)
