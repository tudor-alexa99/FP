
class Ai():
    def __init__(self, controll_game):
      '''
      The class uses a virtual, secondary game to control all the
      possible moves made by either the computer or the player
      '''
      self.controll_game = controll_game

    def test_win(self, val, options):
        '''
        Simulates adding pieces in each position
        If any of them resul in a victory, return the position
        checks in the ptions to see if the position is available
        '''
        # new_game = Game
        for i in options:
            self.controll_game.board.move(i, val)
            if self.controll_game.victory(i) == True:
                reset = self.controll_game.board._getPosition(i)
                self.controll_game.board.set_value(reset, 0)
                return i
            reset = self.controll_game.board._getPosition(i)
            self.controll_game.board.set_value(reset, 0)
            #returns to the initial value
        return None

    def double_move_possibility(self):
        '''
        Makes 2 imaginary moves. If any of them could result
        in victory, makes it
        '''
        pass