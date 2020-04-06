from board import Board


class Game():
    def __init__(self, board):
        self._board = board

    def __str__(self):
        return self._board.__str__()
    def __copy__(self):
        return self.board
    @property
    def board(self):
        return self._board

    def moveHuman(self, col):
        self._board.move(col, 1)
    def moveComputer(self, col):
        self._board.move(col, -1)


    def victory(self, col):
        '''
        Starting from the last disc added, count the number of discs
        in the same line, in all the  directions
        left/right/up/down
        'LU'/'LD'/'RU'/'RD'
        '''
        pos = self.board._getPosition(col)
        UD = LR = 1
        #up-down / left-right
        LU_RD = LD_RU = 1
        '''
        pos will be the element on top of the column
        '''
        if self.board[pos] != 0 :
            LR += self._goLeft(pos)
            LR += self._goRight(pos)
            UD += self._goUp(pos)
            UD += self._goDown(pos)

        if LR >=4 or UD >= 4:
            return True

        LU_RD += self._goLU(pos)
        LU_RD += self._goRD(pos)
        LD_RU += self._goLD(pos)
        LD_RU += self._goRU(pos)

        if LU_RD >= 4 or LD_RU >= 4:
            return True
        return False

    def _goLeft(self, pos):
        count = 0
        if pos % 7 == 0:
            # means we're on the left side
            return 0
        i = pos - 1
        while self.board.leftEdge(i) == False and self._board[i] == self._board[pos]:
            count += 1
            i -= 1
        if self.board.leftEdge(i) == True and self._board[i] == self._board[pos]:
            return count + 1
        return count

    def _goRight(self, pos):
        count = 0
        if pos % 7 == 6:
            # means we're on the right side
            return 0
        i = pos + 1
        while self.board.rightEdge(i) == False and self._board[i] == self._board[pos]:
            count += 1
            i += 1
        if self.board.rightEdge(i) == True and self._board[i] == self._board[pos]:
            return count + 1
        return count

    def _goUp(self, pos):
        count = 0
        if pos in range(0, 7):
            # means we're on top of the column
            return 0
        i = pos - 7
        while self.board.upperEdge(i) == False and self._board[i] == self._board[pos]:
            count += 1
            i -= 7
        if self.board.upperEdge(i) == True and self._board[i] == self._board[pos]:
            return count + 1
        return count

    def _goDown(self, pos):
        count = 0
        if pos in range(35, 43):
            # means we're on the bottom of the column
            return 0
        i = pos + 7
        while self.board.lowerEdge(i) == False and self._board[i] == self._board[pos]:
            count += 1
            i += 7
        if self.board.lowerEdge(i) == True and self._board[i] == self._board[pos]:
            return count + 1
        return count

    def _goRD(self, pos):
        if self.board.lowerEdge(pos) == True or self.board.rightEdge(pos) == True:
            return 0
        else:
            count = 0
            i = pos + 8
            while self.board.rightEdge(i) == False and self.board.lowerEdge(i) == False and self._board[i] == self._board[pos]:
                count += 1
                i += 8
                if i > 41:
                    return count
            if (self.board.rightEdge(i) == True or self.board.lowerEdge(i) == True) and self._board[i] == self._board[pos]:
                return count + 1
            return count

    def _goLU(self, pos):
        # if pos in range(0,7):
        if self.board.upperEdge(pos) == True or self.board.leftEdge(pos) == True:
            return 0
        count = 0
        i = pos - 8
        while self.board.upperEdge(i) == False and self.board.leftEdge(i) == False and self._board[i] == self._board[pos]:
            count += 1
            i -= 8
            if i < 0:
                return count
        if (self.board.leftEdge(i) == True or self.board.upperEdge(i) == True) and self._board[i] == self._board[pos]:
            return count + 1
        return count


    def _goRU(self, pos):
        if self.board.upperEdge(pos) == True or self.board.rightEdge(pos) == True:
            return 0
        count = 0
        i = pos - 6
        while self.board.upperEdge(i) == False and self.board.rightEdge(i) == False and self.board[i] == self.board[pos]:
            count += 1
            i -= 6
        if self.board.upperEdge(i) == True or self.board.rightEdge(i) == True:
            if self.board[i] == self.board[pos]:
                return count + 1
        return count

    def _goLD(self, pos):
        if self.board.lowerEdge(pos) == True or self.board.leftEdge(pos) == True:
            return 0
        count = 0
        i = pos + 6
        while self.board.lowerEdge(i) == False and self.board.leftEdge(i) == False and self._board[i] == self._board[pos]:
            count += 1
            i += 6
        if self.board.lowerEdge(i) == True or self.board.leftEdge(i) == True:
            if self.board[i] == self.board[pos]:
                return count + 1
        return count

def test_victory():
    board = Board()
    game = Game(board)
    board.move(2,-1)
    board.move(3,-1)
    board.move(4,-1)
    board.move(5,-1)
    print(game)
    #print(game.victory(5))
    #works

    board.move(3,-1)
    board.move(4,-1)
    board.move(5,1)
    board.move(5,1)
    board.move(5,1)
    board.move(4,1)
    board.move(6,1)
    board.move(6,-1)
    board.move(6,1)
    board.move(6,-1)
    board.move(6,1)
    print(game)
    print(game.victory(3))

# test_victory()