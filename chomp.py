import numpy as np
import pandas as pd

EMOJI = {-1: '\u2612', 0: ' ', 1: '\u2610'}


class ChompGame:
    def __init__(self):
        pass


    def __repr__(self):
        pass


class Board:
    def __init__(self, rows, cols):
        # Use a 2d array to store board state
        # ones for chocolate, zeros for eaten squares, and -1 for poison
        self.rows = rows
        self.cols = cols
        self.state = np.ones((rows, cols), dtype=int)
        self.state[-1][0] = -1

    def __repr__(self):
        return f'Board({self.rows}, {self.cols})'

    def __str__(self):
        col_idx = range(self.cols)
        row_idx = [chr(letter) for letter in range(65, 65+self.rows)]
        board_emoji = np.array([[EMOJI[val] for val in row] for row in self.state])
        board_df = pd.DataFrame(data=board_emoji, index=row_idx, columns=col_idx)
        return str(board_df)

    def take(self, row, col):
        a = Board
        response = row, col
        for response in Board:
            response[row][col:] = 0














    
class Player:
    def __init__(self, players):
        players = []
        Ready_player_1 = input("enter name choose you")
        Ready_player_2 = input("also enter name you choose")


    def coinflip(self):
        return ("Player one has chosen.Player one is" random.choice(player))



    def __repr__(self):
        return f