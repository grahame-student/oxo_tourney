import random

from oxo_tourney.player.player import Player


class RandomPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board, symbol=None):
        size = board.size
        row = random.randrange(size)
        col = random.randrange(size)
        return [col, row]
