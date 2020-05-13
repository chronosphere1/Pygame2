import pygame
import time
import Resources
import Settings
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
    text_rect.center = width_20_percent, height_10_percent
    Settings.game_display.blit(text_surf, text_rect)
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
        resource.button.draw(Settings.game_display)
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
                if event.button == 1:
                    Resources.button_click(pos)

            # check mouse for hover
            if event.type == pygame.MOUSEMOTION:
                Resources.mouse_over(pos)

        # black background
        Settings.game_display.fill(Settings.black)

        # run machines
        Resources.machine_main()

        # draw everything
        draw_everything()

        # show what's happening
        pygame.display.update()

        # set fps
        Settings.clock.tick(60)


game_loop()
pygame.quit()
quit()
