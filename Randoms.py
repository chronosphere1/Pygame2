import numpy as np
import pygame
import random


# create 3 x 60 x (1-255) array
colour_array = np.random.randint(1, 255, size=(60, 3))

# sort from darkest to lightest colour
colour_array = colour_array[np.argsort(colour_array.sum(axis=1))]

forward = True


# random colour
def random_colour_generator():
    r = random.randint(0, 85)+random.randint(0, 85)+random.randint(0, 85)
    g = random.randint(0, 85)+random.randint(0, 85)+random.randint(0, 85)
    b = random.randint(0, 85)+random.randint(0, 85)+random.randint(0, 85)

    random_colour = (r, g, b)
    return random_colour


class RandomColour:
    def __init__(self):
        self.forward = True
        self.rgb_colour = (255, 0, 255)

    def forward_then_backward(self, frame):
        if self.forward:
            rgb_colour = colour_array[frame-1]
        else:
            rgb_colour = colour_array[60-frame]

        if frame >= 60:
            self.forward = False

        return rgb_colour


player_colour = RandomColour()

