from ai import Ai
from board import Board
from game import Game
from random import choice


class Ui():
    def __init__(self):
        self._board = Board()
        self._other_board = Board()
        self._game = Game(self._board)
        self.control_game = Game(self._other_board)
        # Takes the exact board as the displayed game
        self._ai = Ai(self.control_game)

    def choose_mode(self):
        print("Which way would you like to play?")
        print("\t1.Single Player")
        print("\t2.Multilayer")
        i = input(":")
        if i == "1":
            self.play_single()
        else:
            self.play_multi()
    def play_single(self):
        print(self._game, "\n")
        '''
        Crate a list of available columns for the player and the computer
        '''
        computer_options = [1,2,3,4,5,6,7]
        while True:
            try:
                '''
                Takes the input of the player
                If the column is full, prints it out and takes another input
                '''
                col = int(input("Choose a line to place the disc "))
                available = self._game.board._getPosition(col)

                while available < 7:
                    computer_options.remove(col)
                    col = int(input("Full collumn, please choose again!"))
                    available = self._game.board._getPosition(col)
                # if you place a disc in the last available position of the board.
                # you have to remove that as well from the computer_options
                if available in range(7, 14):  # meaning we used the last available one on the line
                    computer_options.remove(col)

                self._game.moveHuman(col)
                self.control_game.moveHuman(col)
                #make the exact same moves in the control game

                if self._game.victory(col) == True:
                    print(self._game, "\n")
                    print("You won")
                    return
                print(self._game, "\n")

                '''
                p2 will be the computer's move
                First, it checks whether a disc can be placed by the computer 
                in order for it to win
                '''
                p2 = self._ai.test_win(-1, computer_options)
                '''
                If placing a certain disc somewhere cannot make the computer win,
                it checks whether the player has any option to place a disc in order to win 
                and tries to stop it 
                '''
                if p2 == None:
                    p2 = self._ai.test_win(1, computer_options)
                    if p2 != None:
                        print("Blocked you =) ")
                '''
                If the next move can't bring victory to either the player or the
                computer, it chooses a random (available) option
                '''
                if p2 == None:
                    p2 = choice(computer_options)
                    available = self._game.board._getPosition(p2)

                    while available < 7:
                        #if a certain column is occupied, removes it from the options
                        computer_options.remove(p2)
                        p2 = choice(computer_options)
                        available = self._game.board._getPosition(p2)
                    if available in range(7, 14):
                        computer_options.remove(p2)

                self._game.moveComputer(p2)
                self.control_game.moveComputer(p2)
                print(self._game, "\n")
                if self._game.victory(p2) == True:
                    print(self._game, "\n")
                    print("You lost!")
                    return
                p2 = None
            except ValueError:
                print("please insert numbers here")

    def play_multi(self):
        while True:
            print(self._game, "\n")
            try:
                p1 = int (input("Player 1: "))
                self._game.moveHuman(p1)
                print(self._game, "\n")
                if self._game.victory(p1) == True:
                    print("Player 1 wins!")
                    return
                p2 = int(input("Player 2: "))
                self._game.moveComputer(p2)
                print(self._game, "\n")
                if self._game.victory(p2) == True:
                    print("Player 2 wins!")
                    return
            except ValueError as e:
                print(e)
ui = Ui()
ui.choose_mode()