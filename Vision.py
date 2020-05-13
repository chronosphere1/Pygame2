import pygame
import Settings

frame_x = Settings.display_width / 2  # currently 600
frame_y = Settings.display_height / 2  # currently 400


def display():
    # background
    pygame.draw.rect(Settings.game_display, Settings.grey, (frame_x, 0, frame_x, frame_y), 0)
    # draw a grid
    start_line = [frame_x * 1.5, 0]
    end_line = [frame_x * 1.5, frame_y]
    pygame.draw.line(Settings.game_display,
                     Settings.black,
                     start_line,
                     end_line,
                     1)
