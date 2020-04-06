from controller import Controller
from person import Person
from repository import Repository


class Ui:
    def __init__(self):
       self._repo = Repository("person.txt")
       self._controller = Controller(self._repo)

    def print_menu(self):
        pass

    def choose_command(self):
        pass
    def print_all(self):
        for item in self._repo:
            print (item)
    def add_pacient(self):
        id = int(input ("id = "))
        immune = input(" immune = ")
        status = input("status = ")
        pacient = Person(id, immune, status)
        self._controller._add(pacient)
ui = Ui()
ui.print_all()
ui.add_pacient()
ui.print_all()