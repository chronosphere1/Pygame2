import pygame
import Constants

building_list = []


class Building:
    def __init__(self, name, image_location, x, y):
        self.name = name
        self.amount = 1
        self.x = x
        self.y = y

        # loads the image
        self.img = pygame.image.load(image_location)
        # creates a rectangle of the image size
        self.rect = self.img.get_rect().size

        # add to building list
        building_list.append(self)

    # draw the building
    def draw_building(self, x_pos, y_pos):
        # move the image to the right by half the image width
        x_pos += self.rect[0] / 2
        Constants.game_display.blit(self.img, (x_pos, y_pos))


# places the building on the grid
def make_buildings(x_grid, y_grid, x_pos, y_pos):
    if x_grid == water_machine.x \
            and y_grid == water_machine.y:
        water_machine.draw_building(x_pos, y_pos)


water_machine = Building("water_machine", Constants.square_building, x=4, y=6)




