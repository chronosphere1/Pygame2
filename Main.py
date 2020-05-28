import pygame
import time
import Resources
import Constants
import Map
import Units
import sys
import random

pygame.init()


# make both the surf and rect render
def text_objects(text, font):
    text_surface = font.render(text, True, Constants.red)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    # starting position, 20% width, 10% height
    text_rect.center = Constants.WIDTH_20_PERCENT, Constants.HEIGHT_10_PERCENT
    Constants.game_display.blit(text_surf, text_rect)
    # update display
    pygame.display.update()
    # wait 2 secs
    time.sleep(2)
    # start over
    game_loop()


# draw everything
def draw_everything(frame):
    for resource in Resources.resources_list:
        # create the buttons
        resource.button.draw(Constants.game_display)
        # display the amounts
        resource.display_amount()

    # draw player
    Units.make_player(frame)


class Move:
    def __init__(self):
        self.x_change = 0
        self.y_change = 0
        self.key_down = 0.0

    def change(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_RIGHT]:
            self.x_change = 0  # nothing
        elif keys_pressed[pygame.K_LEFT]:
            self.x_change = -1
        elif keys_pressed[pygame.K_RIGHT]:
            self.x_change = 1
        else:
            self.x_change = 0

        if keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]:
            self.y_change = 0
        elif keys_pressed[pygame.K_UP]:
            self.y_change = -1
        elif keys_pressed[pygame.K_DOWN]:
            self.y_change = 1
        else:
            self.y_change = 0



def game_loop(world_map):
    game_exit = False
    frame = 0
    move = Move()

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # mouse position
            pos = pygame.mouse.get_pos()

            # if any key is hit
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_x]:
                Units.x_action()

            # calculate movement
            move.change(keys_pressed)

            # checking the mouse for button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # left mouse button
                if event.button == 1:
                    Resources.button_click(pos)

            # check mouse for hover
            if event.type == pygame.MOUSEMOTION:
                Resources.mouse_over(pos)

        # before moving, check if you've hit the edge, if not, move player
        if (Units.player.x + move.x_change) <= (Constants.FRAME_WIDTH - Units.player.rect[0]) \
                and (Units.player.x + move.x_change >= 0):
            Units.player.x += move.x_change
        if (Units.player.y + move.y_change) <= (Constants.FRAME_HEIGHT - Units.player.rect[1]) \
                and (Units.player.y + move.y_change >= 0):
            Units.player.y += move.y_change

        # create check to see what tile you're on

        # update frame number, 0 to 59?
        if frame >= 60:
            frame = 0
        else:
            frame += 1

        # black background
        Constants.game_display.fill(Constants.black)

        # draw map and grid
        Map.display(world_map)

        # run machines
        Resources.machine_main()

        # draw units and buttons and resource amount
        draw_everything(frame)

        # show what's happening
        pygame.display.update()

        # set fps
        Constants.clock.tick(60)


def main():
    # load map
    world_map = Map.read_map(Constants.map_file)

    game_loop(world_map)


main()
pygame.quit()
quit()
