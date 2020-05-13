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


# button class
class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.text = text

    def draw(self, game_display):
        # Call this method to draw the button on the screen
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


# button actions
# button click
def button_click(pos):
    for resource in resources_list:
        if resource.button.is_over(pos):
            resource.increase(1)


# button mouse over
def mouse_over(pos):
    for resource in resources_list:
        if resource.button.is_over(pos):
            resource.button.color = (195, 195, 195)
        else:
            resource.button.color = (220, 220, 220)


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

    def __init__(self, name, order):
        self.name = name
        self.order = order
        # create resource button
        self.button = Button(color=(220, 220, 220),
                             x=0,
                             y=order * height_10_percent,
                             width=width_20_percent,
                             height=height_10_percent,
                             text=name)
        resources_list.append(self)

    def increase(self, increase_amount):
        self.amount = self.amount + increase_amount
        print("Increased {}".format(self.name))

    def display_amount(self):
        font = pygame.font.SysFont(None, 60)
        text = font.render(str(self.amount), True, white)
        game_display.blit(text, (width_20_percent, self.order * height_10_percent))


# create the base resources; name, position
resources_list = []
water = BaseResource("Water", order=0)
mud = BaseResource("Mud", order=1)
clay = BaseResource("Clay", order=2)


# draw everything
def draw_buttons():
    for resource in resources_list:
        # create the buttons
        resource.button.draw(game_display)
        # display the amounts
        resource.display_amount()


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
                button_click(pos)

            # check mouse for hover
            if event.type == pygame.MOUSEMOTION:
                mouse_over(pos)

        # black background
        game_display.fill(black)

        # draw buttons
        draw_buttons()

        # show what's happening
        pygame.display.update()

        # set fps
        clock.tick(60)


game_loop()
pygame.quit()
quit()
