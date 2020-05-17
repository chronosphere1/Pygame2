import pygame
import Constants


class Unit:
    def __init__(self, name, image_location, x, y):
        self.name = name
        self.amount = 1
        self.x = x
        self.y = y

        # loads the image
        self.img = pygame.image.load(image_location)
        # creates a rectangle of the image size
        self.rect = self.img.get_rect().size

    # draw the player
    def draw_player(self):
        # calculate x and y position
        x_pos = self.x * Constants.BLOCK_WIDTH + Constants.FRAME_WIDTH  # start offset by frame width
        y_pos = self.y * Constants.BLOCK_HEIGHT

        # move the image to the right by half the difference between picture width and block width
        x_pos += (Constants.BLOCK_WIDTH - self.rect[0]) / 2

        # draw image on screen
        Constants.game_display.blit(self.img, (x_pos, y_pos))


# draws the player on the grid
def make_player():
    player.draw_player()


def place_building(building_name):
    if building_name == "Pump":
        print("Lets make a pump")


player = Unit("Goku", Constants.player, x=4, y=5)
