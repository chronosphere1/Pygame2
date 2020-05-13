import pygame
import Button
import Settings


class BaseResource:
    # set resource start amount
    amount = 0

    def __init__(self, name, order):
        self.name = name
        self.order = order
        # create resource button
        self.button = Button.Button(color=(220, 220, 220),
                                    x=0,
                                    y=order * Settings.height_10_percent,
                                    width=Settings.width_20_percent,
                                    height=Settings.height_10_percent,
                                    text=name)
        resources_list.append(self)

    def increase(self, increase_amount):
        self.amount = self.amount + increase_amount
        print("Increased {}".format(self.name))

    # display the resource amount
    def display_amount(self):
        font = pygame.font.SysFont(None, 60)
        text = font.render(str(self.amount), True, Settings.white)
        Settings.game_display.blit(text, (Settings.width_20_percent, self.order * Settings.height_10_percent))


# create the base resources; name, position
resources_list = []
water = BaseResource("Water", order=0)
mud = BaseResource("Mud", order=1)
clay = BaseResource("Clay", order=2)

per_tick = 0


# gives a set amount of resources per tick
def machine_main():
    global per_tick
    per_tick += 1
    if per_tick >= 60:
        water.increase(1)
        per_tick = 0


# button actions
# button click
def button_click(pos):
    for resource in resources_list:
        if resource.button.is_over(pos):
            resource.increase(1)


# button mouse over
def mouse_over(pos):
    for resource in resources_list:
        if resource.button.is_over(pos):
            resource.button.color = (195, 195, 195)
        else:
            resource.button.color = (220, 220, 220)