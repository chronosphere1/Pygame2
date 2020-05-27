import numpy as np
import pygame
import random


# create 3 x 60 x (1-255) array
colour_array = np.random.randint(1, 255, size=(60, 3))

# sort from darkest to lightest colour
colour_array = colour_array[np.argsort(colour_array.sum(axis=1))]


# random colour
def random_colour_generator():
    r = random.randint(0, 85)+random.randint(0, 85)+random.randint(0, 85)
    g = random.randint(0, 85)+random.randint(0, 85)+random.randint(0, 85)
    b = random.randint(0, 85)+random.randint(0, 85)+random.randint(0, 85)

    random_colour = (r, g, b)
    return random_colour


def random_colour_generator2(frame):

    rgb_colour = colour_array[frame-1]
    return rgb_colour

