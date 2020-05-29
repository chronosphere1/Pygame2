import numpy as np
import pygame
import random


# create 3 x 60 x (1-255) array
colour_array = np.random.randint(1, 255, size=(60, 3))

# sort from darkest to lightest colour
colour_array = colour_array[np.argsort(colour_array.sum(axis=1))]


# random colour, returns one random colour
def random_colour_generator():
    r = random.randint(0, 85)+random.randint(0, 85)+random.randint(0, 85)
    g = random.randint(0, 85)+random.randint(0, 85)+random.randint(0, 85)
    b = random.randint(0, 85)+random.randint(0, 85)+random.randint(0, 85)

    random_colour = (r, g, b)
    return random_colour


class RandomColour:
    def __init__(self):
        self.rgb_colour = (255, 0, 255)
        self.slower_count = 0

    def slower(self, frame):
        # only once every 15 frames, the slower counter goes up
        # there's probably a better way to do this
        if frame % 15 == 0:
            if self.slower_count >= 59:
                self.slower_count = 0
            else:
                self.slower_count += 1

        self.rgb_colour = colour_array[self.slower_count]

        return self.rgb_colour


# create player colour
player_colour = RandomColour()

