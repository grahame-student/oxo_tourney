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
        row = 0
        col = 0
        board_state = f"{board}".splitlines()
        board_state = "".join(board_state)

        available_spaces = []
        for var in range(size * size):
            if board_state[var] == '.':
                available_spaces.append(var)

        element = random.choice(available_spaces)
        
        for var in range(size):
            if element < (size * (var + 1)) and (element >= (size * var)):
                row = element - (size * var)
                col = var

        return [row, col]