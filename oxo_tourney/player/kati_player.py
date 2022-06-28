from oxo_tourney.player.player import Player
import random


# Create new player class from this template
# Add a line for your player class to the __init__.py file
# Implement your version of the get_move function

class KatiPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board, symbol):
        # fluff code for basic testing
        size = board.size
        row = random.randrange(size)
        col = random.randrange(size)
        print("kati is playing")
        return [row, col]
