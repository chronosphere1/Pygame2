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
    text_surface = font.render(text, True, red)
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
def draw_everything():
    for resource in Resources.resources_list:
        # create the buttons
        resource.button.draw(Constants.game_display)
        # display the amounts
        resource.display_amount()

    # draw player
    Units.make_player()


def game_loop(world_map):
    game_exit = False

    x_change = 0
    y_change = 0
    ticks_since_move = 0

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

            if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_RIGHT]:
                x_change = 0  # nothing
            elif keys_pressed[pygame.K_LEFT]:
                x_change = -1
            elif keys_pressed[pygame.K_RIGHT]:
                x_change = 1
            else:
                x_change = 0

            if keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]:
                y_change = 0
            elif keys_pressed[pygame.K_UP]:
                y_change = -1
            elif keys_pressed[pygame.K_DOWN]:
                y_change = 1
            else:
                y_change = 0

            # checking the mouse for button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # left mouse button
                if event.button == 1:
                    Resources.button_click(pos)

            # check mouse for hover
            if event.type == pygame.MOUSEMOTION:
                Resources.mouse_over(pos)

        # before moving, check if you've hit the edge, if not, move player
        if (Units.player.x + x_change) <= (Constants.FRAME_WIDTH - Units.player.rect[0]) \
                and (Units.player.x + x_change >= 0):
            Units.player.x += x_change
        if (Units.player.y + y_change) <= (Constants.FRAME_HEIGHT - Units.player.rect[1]) \
                and (Units.player.y + y_change >= 0):
            Units.player.y += y_change

        # black background
        Constants.game_display.fill(Constants.black)

        # run machines
        Resources.machine_main()

        # draw map and grid
        Map.display(world_map)

        # draw everything else
        draw_everything()

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
