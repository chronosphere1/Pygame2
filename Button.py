import pygame


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
            font = pygame.font.SysFont('freesansbold.ttf', 30)
            text = font.render(self.text, 1, (0, 0, 0))
            game_display.blit(text, (self.x + int((self.width / 2 - text.get_width() / 2)),
                                     self.y + int((self.height / 2 - text.get_height() / 2))))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False



