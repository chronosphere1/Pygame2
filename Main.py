import pygame
import time
import Resources
import Constants
import Map
import Units
import math
import sys
import random

pygame.init()

world_map = Map.world_map


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
        self.x_speed = 0
        self.y_speed = 0
        self.key_down = 0.0
        self.max_speed = 1.5
        self.stop_speed = 1
        self.x_slow = True
        self.y_slow = True

    def x_move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_RIGHT]:
            self.x_slow = True
        elif keys_pressed[pygame.K_LEFT]:
            self.x_speed -= self.max_speed
            self.x_slow = False
        elif keys_pressed[pygame.K_RIGHT]:
            self.x_speed += self.max_speed
            self.x_slow = False
        else:
            pass

        # slow down if over max speed
        if abs(self.x_speed) > self.max_speed:
            self.x_speed *= 0.5

    def y_move(self, keys_pressed):
        if keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]:
            self.x_slow = True
        elif keys_pressed[pygame.K_UP]:
            self.y_speed -= self.max_speed
            self.y_slow = False
        elif keys_pressed[pygame.K_DOWN]:
            self.y_speed += self.max_speed
            self.y_slow = False
        else:
            pass

        # slow down if over max speed
        if abs(self.y_speed) > self.max_speed:
            self.y_speed *= 0.5

    # slow down the player slowly
    def slow_down(self):
        slow_down_multiplier = 1 / 5

        if self.x_slow:
            # decrease/increase depending if the value is under 0
            # increase by square root of current number times multiplier
            if self.x_speed >= 0:
                self.x_speed -= math.sqrt(self.x_speed) * slow_down_multiplier
            else:
                self.x_speed += math.sqrt(abs(self.x_speed)) * slow_down_multiplier

            # stop completely if close to stopping
            if -self.stop_speed < self.x_speed < self.stop_speed:
                self.x_speed = 0

        if self.y_slow:
            if self.y_speed >= 0:
                self.y_speed -= math.sqrt(self.y_speed) * slow_down_multiplier
            else:
                self.y_speed += math.sqrt(abs(self.y_speed)) * slow_down_multiplier

            # stop completely if close to stopping
            if -self.stop_speed < self.y_speed < self.stop_speed:
                self.y_speed = 0


def game_loop():
    global world_map
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

                if keys_pressed[pygame.K_x]:
                    Units.x_action()

            # key unpressed
            elif event.type == pygame.KEYUP:
                if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT]:
                    move.x_slow = False
                else:
                    move.x_slow = True

                if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN]:
                    move.y_slow = False
                else:
                    move.y_slow = True

            # mouse position
            pos = pygame.mouse.get_pos()

            # checking the mouse for button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # left mouse button
                if event.button == 1:
                    Resources.button_click(pos)

            # check mouse for hover
            if event.type == pygame.MOUSEMOTION:
                Resources.mouse_over(pos)

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

        # draw map and grid
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

    game_loop()


main()
pygame.quit()
quit()
