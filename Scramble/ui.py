from game import Game

class Ui:
    def __init__(self, filename):
        self.game = Game()
        self.filename = filename

    def commands_menu(self):
        print("Choose yput command: ")
        print("\t1 >>>Insert line: ")
        print("\t2 >>>Start game!")
        print(("\t0 >>Exit"))
        i = input("\n:")
        if i == "0":
            return
        elif i == "1":
            self.add_line()
        elif i == "2":
            self.play_game()
        else:
            print("Invalid input! Please try again!")
            self.commands_menu()

    def add_line(self):
        com = input("Insert a line here: ")
        self.game.add_sentence(com, self.filename)

    def play_game(self):
        pass

ui = Ui("input.txt")
ui.commands_menu()