# Takes the position of the mouse, creates a x*y frame and puts the text in there
import pygame
import Constants


tooltips = {
    "Coin": "This is how much coin you have",
    "Energy": "You need this to power things",
    "Water": "Too much water is probably a bad thing"
}

tip_width = Constants.BLOCK_WIDTH * 10
tip_height = Constants.BLOCK_HEIGHT * 10

# create a surface to draw on
tooltip_surface = pygame.Surface((tip_width, tip_height), pygame.SRCALPHA, 32)


class Tooltip:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.width = Constants.BLOCK_WIDTH * 5
        self.height = Constants.BLOCK_HEIGHT * 5
        self.surface = pygame.Surface((tip_width, tip_height), pygame.SRCALPHA, 32)
        self.visible = False
        self.time = 60
        self.text = "Tips could go here"

    def show_tooltip(self, button_text, pos):  # pos = x, y
        if button_text in tooltips:
            self.visible = True
            self.x = Constants.BLOCK_WIDTH * 6
            self.y = (pos[1] // 30) * 30 + 15
            self.text = tooltips[button_text]
            self.time = 150

    def draw(self):
        if self.visible:
            # put some text on top
            font = Constants.font(24)
            text = font.render(self.text, 1, Constants.light_grey)
            text_rect = text.get_rect()
            text_rect.center = (self.x * 2, self.y)

            Constants.game_display.blit(text, text_rect)
            if self.time > 1:
                self.time -= 1
            else:
                self.visible = False


tooltip = Tooltip()
