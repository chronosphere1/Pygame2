# the main text box where most player messages go
import Constants
import pygame
import Button
import Units
import Resources
import Tooltips


action_list = []


class ActionBox:
    def __init__(self):
        self.height = Constants.DISPLAY_HEIGHT - Constants.FRAME_HEIGHT # 200 at time of writing
        self.width = Constants.FRAME_WIDTH / 2
        self.x = 0
        self.y = Constants.FRAME_HEIGHT
        self.text_surface = pygame.Surface((self.width, self.height))

        self.messages = []

    def draw(self):
        self.text_surface.fill(Constants.alt_blue)

        # draw a rectangle on top of the background colour, 2 pixel from the border
        pygame.draw.rect(self.text_surface, Constants.light_blue, (1, 1, self.width - 3, self.height - 3), 2)

        # display background
        Constants.game_display.blit(self.text_surface, (self.x, self.y))

        # buttons
        font = Constants.font(22)

        for i, message in enumerate(self.messages[:13]):
            text = font.render(message, True, Constants.light_grey)
            # display text
            Constants.game_display.blit(text, (self.x + 2,
                                               Constants.DISPLAY_HEIGHT
                                               - Constants.BLOCK_HEIGHT / 2
                                               - 1
                                               - i * Constants.BLOCK_HEIGHT / 2))


class ActionButton:
    def __init__(self, text_top, text_bottom=''):
        # add to action button list and set order
        action_list.append(self)
        self.order = action_list.index(self)
        self.base_color = Constants.dark_blue
        self.color = self.base_color

        self.name = text_top

        # create button
        self.button = Button.Button(color=self.color,
                                    x=self.order * Constants.BLOCK_HEIGHT * 2,
                                    y=action_box.y,
                                    width=Constants.BLOCK_WIDTH * 2,
                                    height=Constants.BLOCK_HEIGHT * 2,
                                    text_top=text_top,
                                    text_bottom=text_bottom,
                                    font_size=22)


# button click
def button_click(pos):
    for action in action_list:
        if action.button.is_over(pos):
            if action == z_action:
                Resources.water.dump_water()
            elif action == x_action:
                Units.x_action()
            elif action == c_action:
                Resources.sand.sell_sand()


# button mouse over
def mouse_over(pos):
    global action_list
    for action in action_list:
        if action.button.is_over(pos):
            # change colour
            action.button.color = Constants.light_blue
        else:
            action.button.color = action.button.base_color


# load the textbox
action_box = ActionBox()

# create some buttons
z_action = ActionButton("Drop", "Water")
x_action = ActionButton("Dig")
c_action = ActionButton("Sell", "Sand")

