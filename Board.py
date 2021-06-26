from Tile import Tile
from Tile import State
import random

class Board():
    """ This class will hold all values for the board """
    def __init__(self, rows, columns):
        self.rows = rows
        self.colums = columns
        self.board = []
        self.display = ""
        self.create_board()

    def create_board(self):
        current_row = 1
        current_column = 0
        for i in range(self.colums * self.rows):
            current_column += 1
            if i % self.rows == 0:
                current_row += 1
                current_column = 1

            self.board.append(Tile(current_row,current_column, State.EMPTY))
        

        for i in range(5):
            self.board[random.randint(0, len(self.board))].value = State.HUNGRY


        
        devider = "-" * self.rows * 2
        for i in range(len(self.board)):
            if i % self.rows == 0:
                current_row += 1
                self.display += "\n" 
                self.display += f"{devider}\n|"
                current_column = 1
            self.display += f"{self.board[i].value}|"

    def display_board(self):
        print(self.display)
                
