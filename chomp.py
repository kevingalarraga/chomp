import numpy as np
import pandas as pd

EMOJI = {-1: '\u2612', 0: ' ', 1: '\u2610'}


class ChompGame:
    def __init__(self, size=(3, 4)):
        self.p1 = Player()
        self.p2 = Player()
        self.turn = random.choice([self.p1, self.p2])

    def __repr__(self):
        pass

    def play(self):
        players= self.p1 or self.p2
        if self.turn == players:
            return Player(self.name)
            f'You must make the first move'

        players_choice= take from Board

        while players_choice =! self.state[-1][0]:
            return f'Next Players Turn'
        else:
            return f'GAME OVER'




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
        row_idx = [chr(letter) for letter in range(65, 65 + self.rows)]
        board_emoji = np.array([[EMOJI[val] for val in row] for row in self.state])
        board_df = pd.DataFrame(data=board_emoji, index=row_idx, columns=col_idx)
        return str(board_df)

    def take(self, row, col):
        for r in range(row + 1):
            self.state[r][col:] = 0




class Player:
    def __init__(self, score=0, name= 'none'):
        self.score = score
        self.name = input('Enter your name')

    def __repr__(self):
        return f'Player(score={self.score},names={self.names})'
