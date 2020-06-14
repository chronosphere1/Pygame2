import pygame
import time
import Resources
import Tooltips
import Constants
import Map
import Units
import math
import Menu
import Textbox
import Actionbox
import sys
import random

pygame.init()


# draw everything
def draw_everything(frame):
    for resource in Resources.resources_list:
        # create the resource buttons
        resource.button.draw(Constants.game_display)
        # display the resource amounts
        resource.display_amount()
        # draw the tooltips
        Tooltips.tooltip.draw()


    # draw player
    Units.make_player(frame)

    # draw menu if they're active
    Menu.main_menu.draw()

    # draw textbox
    Textbox.textbox.draw()

    # draw bottom left action box
    Actionbox.action_box.draw()

    # draw action buttons
    for action in Actionbox.action_list:
        action.button.draw(Constants.game_display)


class Move:
    def __init__(self):
        self.x_speed = 0
        self.y_speed = 0
        self.key_down = 0.0
        self.max_speed = 1.5
        self.stop_speed = 0.4
        self.x_slow = True
        self.y_slow = True

    def x_move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_RIGHT]:
            self.x_speed = 0.0
        elif keys_pressed[pygame.K_LEFT]:
            self.x_speed -= 0.5
            self.x_slow = False
        elif keys_pressed[pygame.K_RIGHT]:
            self.x_speed += 0.5
            self.x_slow = False
        else:
            pass

    def y_move(self, keys_pressed):
        if keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]:
            self.y_speed = 0
        elif keys_pressed[pygame.K_UP]:
            self.y_speed -= 0.5
            self.y_slow = False
        elif keys_pressed[pygame.K_DOWN]:
            self.y_speed += 0.5
            self.y_slow = False
        else:
            pass

    # slow down the player slowly
    def slow_down(self):
        # slow down if over max speed
        if abs(self.x_speed) > self.max_speed:
            self.x_speed *= 0.995
        # slow down if over max speed
        if abs(self.y_speed) > self.max_speed:
            self.y_speed *= 0.995

        # stop if close to stopping, stops if under stop speed
        if abs(self.x_speed) < self.stop_speed:
            self.x_speed = 0

        if abs(self.y_speed) < self.stop_speed:
            self.y_speed = 0


def game_loop():
    game_exit = False
    frame = 0
    move = Move()

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # if any key is hit
            keys_pressed = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT] \
                        or keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN]:
                    move.x_move(keys_pressed)
                    move.y_move(keys_pressed)

                # main action with x
                if keys_pressed[pygame.K_x]:
                    Units.x_action()

                # menu opening with 'm'
                if keys_pressed[pygame.K_m]:
                    Menu.menu_open_close()

            elif event.type == pygame.KEYDOWN and event.type == event.type == pygame.KEYUP:
                print("Up and down at the same time")

            # mouse position
            pos = pygame.mouse.get_pos()

            # checking the mouse for button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # left mouse button
                if event.button == 1:
                    Resources.button_click(pos)
                    Actionbox.button_click(pos)

            # check mouse for hover
            if event.type == pygame.MOUSEMOTION:
                Resources.mouse_over(pos)
                Actionbox.mouse_over(pos)

        # before moving, check if you've hit the edge, if not, move player
        # if you did hit the edge, bounce back
        if (Units.player.x + move.x_speed) <= (Constants.FRAME_WIDTH - Units.player.rect[0]) \
                and (Units.player.x + move.x_speed >= 0):
            Units.player.x += move.x_speed
        else:
            move.x_speed = -move.x_speed  # reverse speed and half
            move.x_slow = True
        if (Units.player.y + move.y_speed) <= (Constants.FRAME_HEIGHT - Units.player.rect[1]) \
                and (Units.player.y + move.y_speed >= 0):
            Units.player.y += move.y_speed
        else:
            move.y_speed = -move.y_speed  # reverse speed and half
            move.y_slow = True

        # slow down player movement
        move.slow_down()

        # update tile you're on
        Units.player.update_grid_location()

        # update frame number, 0 to 59?
        if frame >= 60:
            frame = 0
        else:
            frame += 1

        # black background
        Constants.game_display.fill(Constants.black)

        # draw map
        Map.display()

        # run machines
        Resources.machine_main()

        # draw units and buttons and resource amount
        draw_everything(frame)

        # show what's happening
        pygame.display.update()

        # set fps
        Constants.clock.tick(60)


def main():
    # initialise the map
    Map.read_map(Constants.map_file)

    game_loop()


main()
pygame.quit()
quit()
