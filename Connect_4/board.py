from text_table import Texttable


class Board():
    def __init__(self):
        self._data = [0] *42
        '''
        position - an elem. on the list
        symbol - X for the player and O for the computer
        '''

    def __str__(self):
        t = Texttable()
        d = {0:" ", -1:"O", 1:"X"}
        for i in range(6):
            lst = self._data[7*i:7*i + 7]
            for j in range(len(lst)):
                lst[j] = d[lst[j]]
            t.add_row(lst)
        rows = []
        for i in range(1,8):
            rows.append(i)
        t.header(rows)
        return t.draw()

    '''
    Make the board iterable
    '''
    def __getitem__(self, item):
        return self._data[item]

    def move(self, col, symbol):
        '''
        Check if the collumn is not full already
        If so, makes a move
        '''
        col -= 1
        ers = self._validate(col)
        if len(ers) != 0:
            raise ValueError(ers)

        pos = self.drop(col)
        #the drop function return the available square from the top of the collumn
        self._data[pos] = symbol
    '''
    The following methods check if the position we're in are in some the edges
    '''
    def leftEdge(self, pos):
        if pos % 7 == 0:
            return True
        return False
    def rightEdge(self,pos):
        if pos %7 == 6:
            return True
        return False
    def upperEdge(self, pos):
        if pos in range(7):
            return True
        return False
    def lowerEdge(self,pos):
        if pos in range(35, 43):
            return True
        return False

    def drop(self, col):
        '''
        The player chooses a column to place the disk
        The function computes the lowes free position to place the disk
        and returns it
        '''

        '''
        COL IS ALREADY DECREMENTED 
        '''

        line = 0
        while col + line < 42 and self._data[col + line] == 0:
            line += 7
        return line+col - 7

    def _validate(self,col):
        e = []
        if self._data[col] != 0:
            e.append("Full collumn!")
        if col < 0 or col > 6:
            e.append("The column must be in between 1 and 7!")
        return e

    def _getPosition(self, col):
        '''
        Returns the last position occupied from the column
        (basically, the "top of the stack"
        '''
        '''
        COL -= 1
        '''
        row = 0
        col -= 1
        while row + col <42 and self._data[row+col] == 0:
            col += 7
            if row+col >= 42:
                return row+col - 7
        return row + col
    def set_value(self, pos, val):
        self._data[pos] = val

def test_print():
    board = Board()
    print(board)

