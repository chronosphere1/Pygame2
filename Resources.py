import pygame
import Button
import Constants
import time


class BaseResource:
    # set resource start amount
    amount = 0

    def __init__(self, name):
        self.name = name
        self.max = 20.0
        self.base_increase = 1/60
        self.text_colour = Constants.white

        # add to resources list
        resources_list.append(self)
        self.order = resources_list.index(self)

        # create resource button
        self.button = Button.Button(color=(220, 220, 220),
                                    x=0,
                                    y=self.order * Constants.HEIGHT_10_PERCENT,
                                    width=Constants.WIDTH_20_PERCENT,
                                    height=Constants.HEIGHT_10_PERCENT,
                                    text=name)

    def increase(self, increase_amount):
        # if it's under the maximum amount, increase
        if self.amount + increase_amount <= self.max:
            self.amount += increase_amount
        # else set to maximum
        elif self.amount + increase_amount > self.max:
            self.amount = self.max

    def decrease(self, decrease_amount):
        # if the decrease amount doesn't take the total to under 0
        if self.amount - decrease_amount >= 0:
            self.amount -= decrease_amount
        # else set to 0
        else:
            self.amount = 0

    def button_click(self):
        if self == dirty_water:
            self.increase(1)
        elif self == water:
            water_button()
        else:
            print("'{}' button clicked but nothing happened".format(self.name))

    # display the resource amount
    def display_amount(self):
        font = pygame.font.SysFont(None, 60)
        # display amount as text, rounded to 1 digit
        text = font.render(str(round(self.amount, 1)), True, self.text_colour)
        x_pos = Constants.WIDTH_20_PERCENT + 10
        y_pos = Constants.HEIGHT_10_PERCENT * self.order + Constants.HEIGHT_10_PERCENT * .25
        Constants.game_display.blit(text, (x_pos, y_pos))


class Energy(BaseResource):
    def __init__(self, name):
        # call base Resource
        super().__init__(name)
        self.amount = 20

    def recalculate(self):
        self.increase(self.base_increase)


# create the base resources; name, position
resources_list = []
money = BaseResource("Coin")
energy = Energy("Energy")
dirty_water = BaseResource("Dirty Water")
water = BaseResource("Water")
Electrolyse = BaseResource("Electrolyse")
clay = BaseResource("Clay")
sand = BaseResource("Sand")


# does a certain amount of things per tick
def machine_main():
    dirty_water.increase(dirty_water.base_increase)
    energy.recalculate()


def water_button():
    water_cost = 20.0
    energy_cost = 10
    if (dirty_water.amount >= water_cost
            and energy.amount >= energy_cost):
        water.increase(1)
        dirty_water.decrease(20)
        energy.decrease(10)


def electrolyse_button():
    pass


# button click
def button_click(pos):
    for resource in resources_list:
        if resource.button.is_over(pos):
            # trigger the button click
            resource.button_click()


# button mouse over
def mouse_over(pos):
    for resource in resources_list:
        if resource.button.is_over(pos):
            resource.button.color = (195, 195, 195)
        else:
            resource.button.color = (220, 220, 220)

