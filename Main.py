import pygame
import time
import sys
import random

pygame.init()

# RBG colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
grey = (195, 195, 195)

# set resolution
display_width = 1200
display_height = 800
game_display = pygame.display.set_mode((display_width, display_height))
#  sizes
width_20_percent = int(display_width / 5)
height_10_percent = int(display_height / 10)

# window title
pygame.display.set_caption('pygame2')
# game clock
clock = pygame.time.Clock()


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.text = text

    def draw(self, game_display, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(game_display, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(game_display, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('freesansbold.ttf', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            game_display.blit(text, (self.x + int((self.width / 2 - text.get_width() / 2)),
                                     self.y + int((self.height / 2 - text.get_height() / 2))))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


# make both the surf and rect render
def text_objects(text, font):
    text_surface = font.render(text, True, red)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    # starting position, 20% width, 10% height
    text_rect.center = width_20_percent, height_10_percent
    game_display.blit(text_surf, text_rect)
    # update display
    pygame.display.update()
    # wait 2 secs
    time.sleep(2)
    # start over
    game_loop()


class BaseResource:
    # set resource start amount
    amount = 0

    def __init__(self, name):
        self.name = name
        # create resource button
        self.button = Button(color=(220, 220, 220),
                             x=0,
                             y=0,
                             width=width_20_percent,
                             height=height_10_percent,
                             text=name)

    def increase(self, increase_amount):
        self.amount = self.amount + increase_amount
        print("Increased {}".format(self.name))

    def display_amount(self):
        font = pygame.font.SysFont(None, 60)
        text = font.render(str(self.amount), True, white)
        game_display.blit(text, (width_20_percent, 0))


# create the base resources, amount 0
water = BaseResource("Water")
muddy_water = BaseResource("Muddy water")




# draw button
def draw_button():
    # create the button
    water.button.draw(game_display, (0, 0, 0))
    # display the amount
    water.display_amount()


def game_loop():
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # mouse position
            pos = pygame.mouse.get_pos()

            # if any key is hit
            keys_pressed = pygame.key.get_pressed()

            # checking the mouse for button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if water.button.is_over(pos):
                    water.increase(1)
                    print("Total water: {}".format(water.amount))

            # check mouse for hover
            if event.type == pygame.MOUSEMOTION:
                if water.button.is_over(pos):
                    water.button.color = (195, 195, 195)
                else:
                    water.button.color = (220, 220, 220)

        # black background
        game_display.fill(black)

        # draw buttons
        draw_button()

        # show what's happening
        pygame.display.update()

        # set fps
        clock.tick(60)


game_loop()
pygame.quit()
quit()
