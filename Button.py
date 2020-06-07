import pygame
import Constants
import Tooltips


# button class
class Button:
    def __init__(self, color, x, y, width, height, text='', font_size=28):
        self.base_color = color
        self.color = color
        self.light_color = Constants.light_blue
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.text = text
        self.font_size = font_size

    def draw(self, game_display):
        # draw a rectangle
        pygame.draw.rect(game_display, self.color, (self.x, self.y, self.width, self.height), 0)

        # draw a rectangle with a border of 2 on top
        pygame.draw.rect(game_display, self.light_color, (self.x + 1, self.y + 1, self.width - 3, self.height - 3), 2)

        if self.text != '':
            font = Constants.font(self.font_size)
            text = font.render(self.text, 1, Constants.light_grey)
            game_display.blit(text, (self.x + int((self.width / 2 - text.get_width() / 2)),
                                     self.y + int((self.height / 2 - text.get_height() / 2))))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                # update the tooltip
                Tooltips.tooltip.show_tooltip(self.text, pos)
                return True
        return False



