import random
from oxo_tourney.player.player import Player


# Create new player class from this template
# Add a line for your player class to the __init__.py file
# Implement your version of the get_move function


def get_position(board, symbol, size):
    available_spaces = []
    for var in range(size * size):
        if board[var] == '.':
            available_spaces.append(var)

    return random.choice(available_spaces)


def convert_position_to_row_and_col(element, size):
    for var in range(size):
        if element < (size * (var + 1)) and (element >= (size * var)):
            row = element - (size * var)
            col = var

    return [row, col]


class KatiPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board, symbol):
        size = board.size
        board_state = f"{board}".splitlines()
        board_state = "".join(board_state)

        element = get_position(board_state, symbol, size)

        move = convert_position_to_row_and_col(element, size)
        print("kt")
        return [move[0], move[1]]
