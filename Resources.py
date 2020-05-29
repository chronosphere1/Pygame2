import pygame
import Button
import Constants
import time


class Unit:
    # set resource start amount
    amount = 0.0

    def __init__(self, name):
        self.name = name
        self.cost = 10
        self.max = 20.0
        self.base_increase = 1/60
        self.text_colour = Constants.white

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
            self.amount = 0.0

    def try_action(self):
        action_succeeded = False
        if energy.amount >= self.cost:
            print("Increased {}".format(self.name))
            self.increase(1.0)
            energy.decrease(10)
            action_succeeded = True
        else:
            print("Not enough energy, need {}, have {}".format(self.cost, energy.amount))

        return action_succeeded


    def button_click(self):
        print("'{}' button clicked but nothing happened".format(self.name))


# resources class
class BaseResource(Unit):
    def __init__(self, name):
        # call base resources
        super().__init__(name)

        # add to resources list and set order
        resources_list.append(self)
        self.order = resources_list.index(self)

        # create resource button
        self.button = Button.Button(color=(220, 220, 220),
                                    x=0,
                                    y=self.order * Constants.HEIGHT_5_PERCENT,
                                    width=Constants.WIDTH_10_PERCENT,
                                    height=Constants.HEIGHT_5_PERCENT,
                                    text=name)

    # display the resource amount
    def display_amount(self):
        font = pygame.font.SysFont(None, 30)
        # display amount as text, rounded to 1 digit
        text = font.render(str(round(self.amount, 1)), True, self.text_colour)
        x_pos = Constants.WIDTH_10_PERCENT + 10
        y_pos = Constants.HEIGHT_5_PERCENT * self.order + Constants.HEIGHT_5_PERCENT * .25
        Constants.game_display.blit(text, (x_pos, y_pos))


# machine class
class BaseMachine(Unit):
    def __init__(self, name):
        # call base resources
        super().__init__(name)

        # set machine cost
        self.cost = 1

        # create machine button
        self.button = Button.Button(color=(220, 220, 220),
                                    x=Constants.DISPLAY_WIDTH / 2,
                                    y=Constants.DISPLAY_HEIGHT / 2,
                                    width=Constants.WIDTH_10_PERCENT,
                                    height=Constants.HEIGHT_10_PERCENT,
                                    text=name)

    def machine_click(self):
        # check for conditions if the building can be placed
        if coin.amount >= self.cost:
            coin.amount -= self.cost
        else:
            print("Not enough coin, needed {} but have only {}".format(self.cost, coin. amount))


# energy class
class Energy(BaseResource):
    def __init__(self, name):
        # call base Resource
        super().__init__(name)
        self.amount = 20

    def recalculate(self):
        self.increase(self.base_increase)


# create the base resources; name, position
resources_list = []
coin = BaseResource("Coin")
energy = Energy("Energy")
water = BaseResource("Water")
sand = BaseResource("Sand")

# set energy cost
sand.cost = 10
water.cost = 1

# give some coin
coin.amount = 1


# does a certain amount of things per tick
def machine_main():
    energy.recalculate()


def x_action(tile_terrain):
    if tile_terrain == "s":
        if sand.try_action():
            pass

    if tile_terrain == "-":
        if water.try_action():
            pass

    if tile_terrain == "x":
        print("Standing on deep water")


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

