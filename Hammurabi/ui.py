from game import Game
import random

class Ui:
    def __init__(self, year):
        self.feed_population = 0
        self.game = Game()
        self.year = year
        self.plant_acres = 0
        self.buy_sell = 0
        # self.s_b_acres = 0
        # self.plant_acres = 0

    def report_message(self):
        print(
            "In year ", self.year, ",", self.game.starved, " people starved.\n",
            self.game.newPeople, " came to the city.\n",
            "City population is ", self.game.population, "\n",
            "City owns ",self.game.land, "acres of land\n",
            "Harvest was ", self.game.harvest, " units per acre.\n",
            "Rats ate ", self.game.rats, " units.\n ",
            "Land price is ", self.game.landPrice, "units per acre\n\n"
            "Grain stocks are ", self.game.grain, "units\n"
              )

    def new_grain(self):
        self.game.set_grain(self.game.grain + self.game.harvest*self.plant_acres - self.game.rats)

    def player_input(self):
        try:
            self.buy_sell = int(input("Acres to buy / sell ->"))
            self.feed_population = int(input("Grains to feed the population: "))
            self.plant_acres = int(input("Acres to plant ->:"))
            self.next_year()
        except ValueError:
            print("invalid input")
            self.player_input()
    def next_year(self):
        self.game.set_landPrice(random.choice(range(15,26)))
        self.game.set_harvest(random.choice(range(1,7)))
        self.feed()
        self.buy_land()

    def buy_land(self):
        if self.game.grain - (self.game._landPrice * self.buy_sell) < 0:
            raise ValueError
        elif self.game.land - self.buy_sell < 0:
            raise ValueError
        else:
            self.game.set_grain(self.game.grain - self.game.landPrice*self.buy_sell)
            self.game.set_land(self.game.land + self.buy_sell)
    def feed(self):
        if self.game.population > self.feed_population//20:
            self.game.set_starved(self.game.population - self.feed_population//20)
            self.game.set_population(self.game.population- self.game.starved)
            self.game.set_newPeople(0)
        else:
            self.game.set_newPeople(random.choice(range(0,11)))
        self.game.set_grain(self.game.grain - self.feed_population)
        self.game.set_population(self.game.population + self.game.newPeople)
year = 0
ui = Ui(year)
while year<5:
    ui.new_grain()
    ui.next_year()
    ui.report_message()
    ui.player_input()
    year += 1