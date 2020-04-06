from texttable import Texttable


class Coffee:
    def __init__(self, price):
        self.price = price

class CreamCoffe(Coffee):
    def __init__(self,price, cream):
        Coffee.__init__(self,price)
        self.cream = cream
    def buy_coffe(self):
        return self.price + self.cream

class MilkCoffee(CreamCoffe):
    def __init__(self,price, cream, milk):
        CreamCoffe.__init__(self,price,cream)
        self.milk = milk

    def buy_coffee(self):
        return self.price + self.milk

#coffee = Coffee()
#m_coffee = MilkCoffee(coffee, 1)
#print(m_coffee.buy_coffee())
coffee = MilkCoffee(5.0, 0.5, 0.4)
cof2= MilkCoffee(coffee, 0.3)
print(coffee.buy_coffe())

class Board:
    def __init__(self, filename):
        self.data = [[" "]*5 for i in range(5)]
        self.filename = filename
    def draw_board(self):
        t = Texttable()
        for i in range(5):
            t.add_row(self.data[i])
        head = ["A","B","C","D", "E"]
        t.header(head)
        return t.draw()

    def add_X(self, i,j):
        for a in range(i):
            for b in range(j):
                self.data[a][b] = "X"

    def some_square(self, l1,c1,l2,c2, symbol):
        for i in range(l1,l2):
            for j in range(c1,c2):
                self.data[i][j] = symbol

    def readFromFile(self):
        fd = open(self.filename, "r")
        symb = {"-": " ", "+":"O"}
        line = fd.readline()
        i = 0
        while len(line):
            for j in range(5):
                self.data[i][j] = symb[line[j]]
            i += 1
            line = fd.readline()
        fd.close()
b = Board("input.txt")
b.add_X(1,1)

# b.some_square(1,1,3,3, "O")
b.readFromFile()
print(b.draw_board())

'''
Let's read a board from a file
'''
