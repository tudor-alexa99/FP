from texttable import *
from random import choice
# draw the board

# Class Board()
#   ---> pune piese pe tabla

# Class Game()

class Board():
    def __init__(self):
        self._data = [[" "]*6 for i in range(6) ]

    def __str__(self):
        t = Texttable()
        for line in range(6):
            t.add_row(self._data[line])

        header = ["T", "U","D","O","R", " "]
        t.header(header)
        # t.header([1,2,3,4,5]
        return t.draw()
    def move(self, r,c,s):
        '''
        :param r: row
        :param c: column
        :param s: symbol
        '''
        self._data[r][c] = s
    def empty_square(self,r,c):
        return self._data[r][c] == " "
    def get_value(self,r,c):
        return self._data[r][c]

    # def val(self,i,j):
    #     return self._data[i][j]




class Game():
    def __init__(self):
        self.board = Board()

    def make_move(self,r,c,s):
        self.board.move(r,c,s)

    def player_won(self,r,c,s):
        '''
        data[r][c]
        look up, down, left, right and on the diagonals for the same symbols as in
        data[r][c] (if nonempty)
        '''
        left_righ = 0
        up_down = 0
        lu_rd = 0
        ld_ru = 0

        left_righ += self._goLeft(r,c,s)
        left_righ += self._goRight(r,c,s)
        up_down += self._goUp(r,c,s)
        up_down += self._goDown(r,c,s)

        if left_righ >= 4:
            return True
        if up_down >= 4:
            return True
        if lu_rd >= 4:
            return True
        if ld_ru >= 4:
            return True

        return False

    def _goLeft(self, r, c, s):
        if c == 0:
            return 0
        same = 0
        j = c-1
        while j >= 0 and self.board.get_value(r,j) == s:
            same += 1
            j -= 1
        return same
    def _goRight(self, r, c, s):
        if c == 5:
            return 0
        same = 0
        j = c+1
        while j <= 5 and self.board.get_value(r,j) == s:
            same += 1
            j += 1
        return same
    def _goUp(self,r,c,s):
        if r == 0:
            return 0
        same = 0
        i = r-1
        while i>= 0 and self.board.get_value(i,c) == s:
            same += 1
            i -= 1
        return same

    def _goDown(self, r, c, s):
        if r == 5:
            return 0
        same = 0
        i = r + 1
        while i <= 5 and self.board.get_value(i, c) == s:
            same += 1
            i += 1
        return same

    def full_board(self):
        for i in range(6):
            for j in range(6):
                if self.board.empty_square(i,j):
                    return False
        return True

    def computer_move(self):
        '''
        First, check if the player can win
        '''

        squares = []
        for i in range(6):
            for j in range(6):
                if self.board.empty_square(r,c):
                    squares.append([i,j])
        '''
        The list of all empty squares
        If there is a move the player can make to win, the computer
        will block it
        
        Else, it will make a random move
        '''
        symbols = ["X","O"]
        for square in squares:
            i = square[0]
            j = square[1]
            if self.player_won(i,j,"X"):
                self.board.move(i,j,"O")
            elif self.player_won(i,j,"O"):
                self.board.move(i,j,"X")
            else:
                #generate a random, but valid move:
                sqr = choice(squares)
                r = sqr[0]
                c = sqr[1]
                s = choice("X", "O")
                self.board.move(r,c,s)


