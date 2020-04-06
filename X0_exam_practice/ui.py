from game import Game


class Ui():
    def __init__(self):
        self.game = Game()

    def start_menu(self):
        print("Choose an option:\n")
        print("\t1.Start new game")
        print("\t2.Load saved game")
        print("\t0.Exit")

        i = input(":")

        if i == "1":
            self.new_game()
        elif i == "2":
            self.load_saved_game()
        elif i =="0":
            return
        else:
            print("Invalid input!")
            self.start_menu()

    def new_game(self):
        print(self.game.board)
        while self.game.full_board() == False and self.game.player_won() == False:
            self.input_commands()
            self.game.computer_move()

    def load_saved_game(self):
        pass

    def input_commands(self):
        r = input("Insert row: ")
        c= input("Insert column: ")
        s = input("Insert symbol: ")
        not_valid = self.check_input(r,c,s)
        if len(not_valid) != 0:
            print(not_valid)
            self.input_commands()
        r = int(r)
        c = int(c)
        self.game.board.move(r,c,s)

        if self.game.player_won():
            print("You won")
            return

        if self.game.full_board():
            print("Full Board!")
            return

    def check_input(self,r,c,s):
        e = [] # a list of all possible errors

        try:
            r = int(r)
            c = int(c)
        except ValueError:
            e.append("The rows and columns must be integers!")
            return e
        if s != "O" and s != "X":
            e.append("Choose a symbol between X and O!")
            return e
        if r not in range(6) or c not in range(6):
            e.append("The rows and columns must be in range 6")
        if self.game.board.empty_square(r,c) != True:
            e.append("Not an empty square")
        return e



ui = Ui()
ui.start_menu()

