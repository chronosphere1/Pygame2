import pygame
import Constants

building_list = []


class Building:
    def __init__(self, name, image_location, x, y):
        self.name = name
        self.amount = 1
        self.x = x
        self.y = y

        self.img = pygame.image.load(image_location)
        # add to building list
        building_list.append(self)

        # print("Can't find building image: {}".format(image_location)

    def draw_building(self):
        Constants.game_display.blit(self.img, (self.x, self.y))


def make_buildings():
    water_machine = Building("water_machine", Constants.square_building, 880, 220)


def show_building():
    for x in range(len(building_list)):
        building_list[x].draw_building()

