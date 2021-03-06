import pygame
import Constants
import Tooltips


# button class
class Button:
    def __init__(self, color, x, y, width, height, text_top='', text_bottom='', font_size=28):
        self.color = color
        self.light_color = Constants.light_blue
        self.light_base_color = Constants.light_blue
        self.highlight_color = Constants.light_grey
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.text_top = text_top
        self.text_bottom = text_bottom
        self.font_size = font_size

    def draw(self, game_display):
        # draw a rectangle
        pygame.draw.rect(game_display, self.color, (self.x, self.y, self.width, self.height), 0)

        # draw a rectangle with a border of 2 on top
        pygame.draw.rect(game_display, self.light_color, (self.x + 1, self.y + 1, self.width - 3, self.height - 3), 2)

        # check lines and display text
        if self.text_top != '':
            # if one lines is given
            if self.text_bottom == '':
                font = Constants.font(self.font_size)
                text = font.render(self.text_top, 1, Constants.light_grey)
                game_display.blit(text, (self.x + int((self.width / 2 - text.get_width() / 2)),
                                         self.y + int((self.height / 2 - text.get_height() / 2))))
            # or two lines are given
            elif self.text_bottom != '':
                # top

                font = Constants.font(self.font_size)
                text = font.render(self.text_top, 1, Constants.light_grey)
                game_display.blit(text, (self.x + int((self.width / 2 - text.get_width() / 2)),
                                         self.y + int((self.height / 3 - text.get_height() / 2))))

                # bottom
                font = Constants.font(self.font_size)
                text = font.render(self.text_bottom, 1, Constants.light_grey)
                game_display.blit(text, (self.x + int((self.width / 2 - text.get_width() / 2)),
                                         self.y + int((self.height / 3 * 2 - text.get_height() / 2))))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                # update the tooltip
                Tooltips.tooltip.show_tooltip(self.text_top, pos)
                return True
        return False



