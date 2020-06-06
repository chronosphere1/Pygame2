# the main text box where most player messages go
import Constants
import pygame


class Textbox:
    def __init__(self):
        self.height = Constants.DISPLAY_HEIGHT - Constants.FRAME_HEIGHT # 200 at time of writing
        self.width = Constants.FRAME_WIDTH / 2
        self.x = Constants.FRAME_WIDTH / 2
        self.y = Constants.FRAME_HEIGHT
        self.text_surface = pygame.Surface((self.width, self.height))

        self.messages = []

    def draw(self):
        self.text_surface.fill(Constants.alt_blue)

        # draw a rectangle on top of the background colour, 2 pixel from the border
        pygame.draw.rect(self.text_surface, Constants.light_blue, (1, 1, self.width - 3, self.height - 3), 2)

        # display background
        Constants.game_display.blit(self.text_surface, (self.x, self.y))

        # display message
        font = Constants.font(22)

        for i, message in enumerate(self.messages[:13]):
            text = font.render(message, True, Constants.light_grey)
            # display text
            Constants.game_display.blit(text, (self.x + 2,
                                               Constants.DISPLAY_HEIGHT
                                               - Constants.BLOCK_HEIGHT / 2
                                               - 1
                                               - i * Constants.BLOCK_HEIGHT / 2))

    def add_message(self, message):
        self.messages.insert(0, (str(message)))


# load the textbox
textbox = Textbox()


# # make both the surf and rect render
# def text_objects(text, font):
#     text_surface = font.render(text, True, Constants.red)
#     return text_surface, text_surface.get_rect()
#
#
# def message_display(text):
#     large_text = pygame.font.Font('freesansbold.ttf', 115)
#     text_surf, text_rect = text_objects(text, large_text)
#     # starting position, 20% width, 10% height
#     text_rect.center = Constants.WIDTH_20_PERCENT, Constants.HEIGHT_10_PERCENT
#     Constants.game_display.blit(text_surf, text_rect)
#     # update display
#     pygame.display.update()
#     # wait 2 secs
#     time.sleep(2)
#     # start over
#     game_loop()