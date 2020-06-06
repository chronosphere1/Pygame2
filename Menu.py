import pygame
import time
import Resources
import Button
import Constants
import math


# FRAME_WIDTH = 1200
# FRAME_HEIGHT = 600

class Menu:
    def __init__(self):
        self.active = False
        self.height = Constants.FRAME_HEIGHT
        self.width = Constants.FRAME_WIDTH // 4
        self.start_x = Constants.FRAME_WIDTH / 4 * 3 + (self.width * 0.55)
        self.x = self.start_x
        self.y = 0
        self.color = Constants.see_through_dark_blue
        self.menu_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)

        self.opening = False
        self.time_since_active = 0

    def draw(self):
        if self.active:
            # opens the menu slowly
            if self.opening:
                self.soft_open()

            self.menu_surface.fill(self.color)

            # draw a rectangle on top of the background colour, 2 pixel from the border
            pygame.draw.rect(self.menu_surface, Constants.see_through_blue, (1, 1, self.width - 2, self.height - 2), 3)

            # display background
            Constants.game_display.blit(self.menu_surface, (self.x, self.y))

            self.add_resources()

        # pygame.draw.rect(menu_surface, self.color, (self.x, self.y, self.width, self.height), 0)

    # add the name, amount and button per resource
    def add_resources(self):
        for i, resource in enumerate(Resources.resources_list):
            font = Constants.font(24)
            text = font.render(resource.name, 1, (225, 225, 225))

            # starting place for x
            start_x = self.x + Constants.BLOCK_WIDTH + 2

            # display resource name
            Constants.game_display.blit(text, (start_x,
                                               i * Constants.BLOCK_HEIGHT + 7))

            # get resource amount
            resource_amount = font.render(str(round(resource.amount, 1)), 1, (195, 195, 195))

            # display resource amount
            Constants.game_display.blit(resource_amount, (start_x + Constants.BLOCK_WIDTH * 3,
                                                          i * Constants.BLOCK_HEIGHT + 7))

            # create sell buttons
            self.sell_button(i, start_x)

    def sell_button(self, i, start_x):
        # create machine button
        button = Button.Button(color=(220, 220, 220),
                               x=start_x + Constants.BLOCK_WIDTH * 5,
                               y=Constants.BLOCK_WIDTH * i,
                               width=Constants.BLOCK_WIDTH * 2,
                               height=Constants.BLOCK_HEIGHT,
                               text="Buy")

        button.draw(Constants.game_display)

    def soft_open(self):
        self.time_since_active += 1

        # if the menu is on the right of the endpoint + 15 pixels
        if self.x >= int((Constants.FRAME_WIDTH / 4 * 3) + 15):
            # formula how much the menu is moving
            self.x -= int(math.sqrt(self.time_since_active)
                          * (self.time_since_active / 4)
                          - (self.time_since_active / 1.5)) + 0.5
        else:
            self.x -= 0.35
            # the end location is met, stop opening
            if int(self.x) <= Constants.FRAME_WIDTH / 4 * 3:
                # making sure exact location
                self.x = Constants.FRAME_WIDTH / 4 * 3
                self.opening = False
                self.time_since_active = 0


# opens and closes the menu
def menu_open_close():
    if not main_menu.active:
        main_menu.active = True
        main_menu.opening = True
    else:  # if the menu is already active, close it
        main_menu.x = main_menu.start_x
        main_menu.active = False
        main_menu.opening = False
        main_menu.time_since_active = 0


main_menu = Menu()
