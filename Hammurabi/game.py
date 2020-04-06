

class Game:
    def __init__(self):
        self._grain = 0
        self._starved = 0
        self._newPeople = 0
        self._population = 100
        self._land = 1000
        self._harvest = 3
        self._landPrice = 20
        self._rats = 200

    @property
    def grain(self):
        return self._grain
    # @property
    # def year(self):
    #     return self._year
    @property
    def newPeople(self):
        return self._newPeople
    @property
    def starved(self):
        return self._starved
    @property
    def population(self):
        return self._population

    @property
    def land(self):
        return self._land

    @property
    def landPrice(self):
        return self._landPrice

    @property
    def harvest(self):
        return self._harvest

    @property
    def rats(self):
        return self._rats

    def set_grain(self, new_val):
        self._grain = new_val

    def set_rats (self, new_val):
        self._rats = new_val
    # def set_year (self, new_val):
    #     self._year = new_val

    def set_newPeople (self, new_val):
        self._newPeople = new_val

    def set_land (self, new_val):
        self._land = new_val

    def set_landPrice (self, new_val):
        self._landPrice = new_val

    def set_harvest (self, new_val):
        self._harvest = new_val

    def set_population (self, new_val):
        self._population = new_val

    def set_starved (self, new_val):
        self._starved = new_val


