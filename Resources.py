import pygame
import Button
import Constants
import Map
import random
import Textbox
import time


class Unit:
    def __init__(self, name):
        self.name = name
        self.amount = 0.0
        self.energy_cost = 10
        self.max = 20.0
        self.base_increase = 1/60
        self.text_colour = Constants.light_grey

    def increase(self, increase_amount):
        # if it's under the maximum amount, increase
        if self.amount + increase_amount <= self.max:
            self.amount += increase_amount
        # else set to maximum
        elif self.amount + increase_amount > self.max:
            self.amount = self.max

    def decrease(self, decrease_amount=1):
        # if the decrease amount doesn't take the total to under 0
        if self.amount - decrease_amount >= 0:
            self.amount -= decrease_amount
        # else set to 0
        else:
            self.amount = 0.0

    def button_click(self):
        print("'{}' button clicked but nothing happened".format(self.name))

        # when the player is standing on sand and actions with main action


# resources class
class BaseResource(Unit):
    def __init__(self, name):
        # call base resources
        super().__init__(name)

        # add to resources list and set order
        resources_list.append(self)
        self.order = resources_list.index(self)

        # create resource button
        self.button = Button.Button(color=Constants.dark_blue,
                                    x=0,
                                    y=self.order * Constants.BLOCK_HEIGHT,
                                    width=Constants.WIDTH_10_PERCENT,
                                    height=Constants.BLOCK_HEIGHT,
                                    text=name)

    # display the resource amount
    def display_amount(self):
        font = Constants.font(30)
        # display amount as text, rounded to 1 digit
        text = font.render(str(round(self.amount, 1)), True, self.text_colour)
        x_pos = Constants.WIDTH_10_PERCENT + 7
        y_pos = Constants.BLOCK_HEIGHT * self.order + 7
        Constants.game_display.blit(text, (x_pos, y_pos))


# energy class
class Energy(BaseResource):
    def __init__(self, name):
        # call base Resource
        super().__init__(name)
        self.amount = 20

    def recalculate(self):
        self.increase(self.base_increase)

    def energy_check(self, resource):
        if self.amount > resource.energy_cost:
            return True
        else:
            Textbox.textbox.add_message(f"Not enough energy to dig {resource.name.lower()}, "
                                        f"need at least {resource.energy_cost}")
            return False


# sand class where all the sand interactions go
class Sand(BaseResource):
    def __init__(self):
        # call base Resource
        super().__init__("Sand")

    # when the player is standing on sand and actions with main action
    def sand_x_action(self, player_x, player_y):
        # check if enough energy
        if energy.energy_check(self):
            # check if not full
            if self.amount < self.max:
                # check if there's sand on the tile
                if Map.map_tile_contents[player_x][player_y].sand > 0 and \
                        self.amount < self.max:
                    # increase sand
                    Textbox.textbox.add_message(f"+1 sand! Sand left: {Map.map_tile_contents[player_x][player_y].sand}")
                    self.increase(1)

                    energy.decrease(self.energy_cost)
                    Map.map_tile_contents[player_x][player_y].dig_sand()
            else:
                Textbox.textbox.add_message(f"You want to dig sand, but you can't carry more than {self.max}")


class Water(BaseResource):
    def __init__(self):
        # call base Resource
        super().__init__("Water")

    def shallow_water_x_action(self, player_x, player_y):
        if self.amount < self.max:
            roll = max(round(random.random() / 2, 1), 0.1)  # minimum of 0.1

            # increase sand
            if sand.amount < sand.max:
                sand.increase(round(roll, 1))
                Textbox.textbox.add_message(f"Dug up +1 water and +{roll} sand")
            else:
                Textbox.textbox.add_message(f"Dug up +1 water and +{roll} sand, "
                                            f"but you don't have room for more sand")

            # remove water
            Map.map_tile_contents[player_x][player_y].dig_shallow_water()

            self.increase(1)
            energy.decrease()
        else:
            Textbox.textbox.add_message(f"Too much water, get rid of your water")

    def dump_water(self):
        Textbox.textbox.add_message(f"You dump all your water, probably in the ocean")
        self.amount = 0.0


# create the resources
resources_list = []
coin = BaseResource("Coin")
energy = Energy("Energy")
water = Water()
sand = Sand()

# set energy cost
sand.energy_cost = 1
water.energy_cost = 1

# give some coin
coin.amount = 1


# does a certain amount of things per tick
def machine_main():
    energy.recalculate()


def x_action(player_x, player_y, tile_terrain):
    if tile_terrain == "s":
        sand.sand_x_action(player_x, player_y)
    elif tile_terrain == "-":
        water.shallow_water_x_action(player_x, player_y)
    elif tile_terrain == "x":
        Textbox.textbox.add_message("Standing on deep water")


# button click
def button_click(pos):
    for resource in resources_list:
        if resource.button.is_over(pos):
            if resource == water:
                water.dump_water()
            else:
                # trigger the button click
                resource.button_click()


# button mouse over
def mouse_over(pos):
    for resource in resources_list:
        if resource.button.is_over(pos):
            resource.button.color = resource.button.light_color  # lighter
        else:
            resource.button.color = resource.button.base_color


