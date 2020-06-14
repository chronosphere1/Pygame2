import numpy as np
import pygame
import random
import math


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

        if frame == 59:
            self.rgb_colour = colour_array[self.slower_count]
            if self.slower_count == 58:
                self.slower_count = 0
            else:
                self.slower_count += 1
        else:
            # find the colour difference and work towards it
            next_colour = colour_array[self.slower_count + 1]
            r_diff = int(next_colour[0] - self.rgb_colour[0]) // 20
            g_diff = int(next_colour[1] - self.rgb_colour[1]) // 20
            b_diff = int(next_colour[2] - self.rgb_colour[2]) // 20

            in_between = [self.rgb_colour[0] + r_diff, self.rgb_colour[1] + g_diff, self.rgb_colour[2] + b_diff]

            self.rgb_colour = tuple(in_between)

        return self.rgb_colour


# create player colour
player_colour = RandomColour()

