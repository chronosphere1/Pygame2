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
        self.energy_cost = 1
        self.max = 20.0
        self.base_increase = 1/60
        self.visible = True
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
        self.visible = True
        self.display_rounding = 1

        # add to resources list and set order
        resources_list.append(self)
        self.order = resources_list.index(self)

        # create resource button
        self.button = Button.Button(color=Constants.dark_blue,
                                    x=0,
                                    y=self.order * Constants.BLOCK_HEIGHT,
                                    width=Constants.WIDTH_10_PERCENT,
                                    height=Constants.BLOCK_HEIGHT,
                                    text_top=name)

    # display the resource amount
    def display_amount(self):
        font = Constants.font(30)
        # display amount as text, rounded to 1 or 3. Can be done in a much better way
        if self.display_rounding == 3:
            text = font.render(str("{:.3f}").format(round(self.amount, self.display_rounding)), True, self.text_colour)
        elif self.display_rounding == 1:
            text = font.render(str("{:.1f}").format(round(self.amount, self.display_rounding)), True, self.text_colour)

        x_pos = Constants.WIDTH_10_PERCENT + 7
        y_pos = Constants.BLOCK_HEIGHT * self.order + 7
        Constants.game_display.blit(text, (x_pos, y_pos))


# energy class
class Energy(BaseResource):
    def __init__(self, name):
        # call base Resource
        super().__init__(name)
        self.amount = 200
        self.max = 200
        self.display_rounding = 3

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
                    Textbox.textbox.add_message(f"+1 sand! Sand left on tile: "
                                                f"{Map.map_tile_contents[player_x][player_y].sand}")
                    self.increase(1)

                    energy.decrease(self.energy_cost)
                    Map.map_tile_contents[player_x][player_y].dig_sand()
            else:
                Textbox.textbox.add_message(f"You want to dig sand, but you can't carry more than {self.max}")

    def sell_sand(self):
        if self.amount < 1:
            Textbox.textbox.add_message(f"Sell what sand? You only have {self.amount}")
        else:
            sell_amount = 1
            sell_price = sell_amount / 10

            self.amount -= sell_amount
            coin.amount += sell_price

            Textbox.textbox.add_message(f"You sell {sell_amount} sand for {sell_price} coin")


class Water(BaseResource):
    def __init__(self):

        # call base Resource
        super().__init__("Water")

    def shallow_water_x_action(self, player_x, player_y):
        # check if enough energy
        if energy.energy_check(self):
            if self.amount < self.max:
                roll = max(round(random.random() / 2, 1), 0.1)  # minimum of 0.1

                # increase sand
                if sand.amount < sand.max:
                    sand.increase(round(roll, 1))
                    Textbox.textbox.add_message(f"Dug up +1 water and +{roll} sand.")
                else:
                    Textbox.textbox.add_message(f"Dug up +1 water and +{roll} sand, "
                                                f"but you don't have room for more sand")

                # remove water
                Map.map_tile_contents[player_x][player_y].dig_shallow_water()

                self.increase(1)
                energy.decrease(self.energy_cost)
            else:
                Textbox.textbox.add_message(f"Too much water, get rid of your water")

    def deep_water_x_action(self, player_x, player_y):
        # check if enough energy
        if energy.energy_check(self):
            if self.amount < self.max:
                self.increase(1)
                energy.decrease(self.energy_cost)
                Textbox.textbox.add_message(f"+1 water")
            else:
                Textbox.textbox.add_message(f"Too much water, get rid of your water")

    def dump_water(self):
        Textbox.textbox.add_message(f"You dump all your water, probably in the ocean")
        self.amount = 0.0


class Filter(BaseResource):
    def __init__(self):
        # call base Resource
        super().__init__("Filter")
        self.amount = 0
        self.cost = 10
        self.energy_cost = 1 / 180
        self.base_increase = 1
        self.ratio = 60
        self.visible = False

    def buy_filter(self):
        if coin.amount >= self.cost:
            coin.amount -= self.cost
            self.amount += self.base_increase
            Textbox.textbox.add_message(f"You buy a filter. It filters sand out of water")
        else:
            Textbox.textbox.add_message(f"A water filter costs {self.cost} but you only have {round(coin.amount, 2)}")

    def get_sand(self):
        # check if the filter has: room for sand; water in inventory; enough energy
        # if so, give sand and reduce the water/energy cost
        water_cost = self.amount / self.ratio / 5

        if sand.amount + sand.base_increase / self.ratio <= sand.max:
            if water.amount >= water_cost:
                if energy.amount >= self.energy_cost * self.amount:
                    energy.amount -= self.energy_cost * self.amount
                    water.amount -= water_cost
                    sand.amount += sand.base_increase / self.ratio


# create the resources
resources_list = []
coin = BaseResource("Coin")
energy = Energy("Energy")
water = Water()
sand = Sand()
water_filter = Filter()

# set energy cost
sand.energy_cost = 1
water.energy_cost = 2

# give some coin
coin.amount = 100


# does a certain amount of things per tick
def machine_main():
    energy.recalculate()
    water_filter.get_sand()


def x_action(player_x, player_y, tile_terrain):
    if tile_terrain == "s":
        sand.sand_x_action(player_x, player_y)
    elif tile_terrain == "-":
        water.shallow_water_x_action(player_x, player_y)
    elif tile_terrain == "x":
        water.deep_water_x_action(player_x, player_y)
    elif tile_terrain == "r":
        Textbox.textbox.add_message(f"Rock. Cool.")


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
            resource.button.light_color = resource.button.highlight_color  # lighter
        else:
            resource.button.light_color = resource.button.light_base_color


