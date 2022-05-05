"""

Objects:
    TicTacToe
    Board

"""
class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.current_player = 'x'
        self.player_to_coord = {'x':[],'o':[]}

    def move(self, row, col):
        if self.board.table[row][col]!='':
            print('AlreadyTakenException')
            return
        self.board.table[row][col] = self.current_player
        self.board.player_to_coord[self.current_player].append((row, col))
        winner = self.board.is_win()
        if winner:
            print (self.current_player, ' player wins!')
            return

        self.change_player()

    def change_player(self):
        if self.current_player == 'x':
            self.current_player = 'o'
        else:
            self.current_player = 'x'

    def printBoard(self):
        print(self.board.table)
        


class Board:
    def __init__(self):
        self.table = [['' for _ in range(3)]for _ in range(3)]
        self.player_to_coord = {'x':[],'o':[]}

    def is_win(self):
        x0, x1, x2 = 0, 0, 0
        y0, y1, y2 = 0, 0, 0

        for key in self.player_to_coord:
            coords = self.player_to_coord[key]
            for coord in coords:
                if coord[0] == 0:
                    x0 += 1 
                elif coord[0] == 1:
                    x1 += 1 
                elif coord[0] == 2:
                    x2 += 1

                if coord[1] == 0:
                    y0 += 1 
                elif coord[1] == 1:
                    y1 += 1 
                elif coord[1] == 2:
                    y2 += 1
                if x0 == 3 or x1 == 3 or x2 == 3:
                    return True 
                if y0 == 3 or y1 == 3 or y2 == 3:
                    return True 
                if y0 == 3 or y1 == 3 or y2 == 3:
                    return True 

            if [(0,0), (1, 1), (2, 2)] in self.player_to_coord[key]:
                return True 
            if [(0,2), (1, 1), (2, 0)] in self.player_to_coord[key]:
                return True 
                
                    

            
ttt = TicTacToe()
ttt.move(0,0)#x
ttt.printBoard()
ttt.move(0,0)#o
ttt.move(1,0)#o
ttt.move(1,1)#x
ttt.move(2,2)#o
ttt.move(2,0)#x
ttt.printBoard()
