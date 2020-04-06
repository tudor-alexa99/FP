
class Controller():
    def __init__(self, repo):
        self._repo = repo
        self._dayCount = []
        #each position will record the number of days
        #for a person

    def _add(self, obj):
        self._repo._add(obj)
        #self._dayCount[len(self._repo)-1] = 0

    def add_day(self):
        for i in range(len(self._repo)):
            self._dayCount += 1
        self.checkDays()
        self.count_sick()

    def checkDays(self):
        for i in range(len(self._repo)):
            if self._dayCount[i] == 7:
                self._repo[i].set_status("Vaccinated")

    def get_sick(self):
        sick = []
        healthy = []
        for i in range(len(self._repo)):
            pacient = self._repo[i]
            if self._dayCount[i] < 7:
                if pacient.status == "":
                    pass
