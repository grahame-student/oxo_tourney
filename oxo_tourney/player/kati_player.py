import random

from oxo_tourney.player.player import Player


PLAYER_1 = "O"
PLAYER_2 = "X"


class KatiPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_other_symbol(symbol):
        other_symbol = "."
        if symbol == PLAYER_1:
            other_symbol = PLAYER_2
        elif symbol == PLAYER_2:
            other_symbol = PLAYER_1
        return other_symbol

    @staticmethod
    def check_rows(board, symbol, size):
        return_value = 0
        count = 0
        # rows
        for var in range(size):
            for ret in range(size):
                # print("r", ret + (size * var), board[ret + (size * var)])
                if board[ret + (size * var)] == symbol:
                    count += 1
                else:
                    count = 0
                if count == size:
                    return_value = 1
        return return_value

    @staticmethod
    def check_columns(board, symbol, size):
        count = 0
        return_value = 0
        # columns
        for var in range(size):
            for ret in range(size):
                # print("c", var + (size * ret), board[var + (size * ret)])
                if board[var + (size * ret)] == symbol:
                    count += 1
                else:
                    count = 0
                if count == size:
                    return_value = 2
        return return_value

    @staticmethod
    def check_diagonals(board, symbol, size):
        count = 0
        return_value = 0
        # diagonal forward
        for var in range(size):
            # print("df", (size + 1) * var,board[((size + 1) * var)])
            if board[((size + 1) * var)] == symbol:
                count += 1
            else:
                count = 0
            if count == size:
                return_value = 3

        count = 0
        # diagonal backward
        for var in range(size):
            # print("db", (size - 1) * (var + 1), board[(size - 1) * (var + 1)])
            if board[(size - 1) * (var + 1)] == symbol:
                count += 1
            else:
                count = 0
            if count == size:
                return_value = 4

        return return_value

    def check_win_board(self, board, symbol, size):
        return_value: int = 0
        return_value += self.check_rows(board, symbol, size)
        return_value += self.check_columns(board, symbol, size)
        return_value += self.check_diagonals(board, symbol, size)
        return return_value

    def check_win_move(self, spaces, board, size, symbol):
        for var in spaces:
            board_copy = board
            board_copy[var] = symbol
            temp = self.check_win_board(board_copy, symbol, size)
            board_copy[var] = "."
            if temp != 0:
                ret = var
                return ret
        return 0xFF

    def get_position(self, board, symbol, size):
        available_spaces = []
        board_state = []
        for var in range(size * size):
            if board[var] == PLAYER_2:
                board_state.append(PLAYER_2)
            elif board[var] == PLAYER_1:
                board_state.append(PLAYER_1)
            else:
                available_spaces.append(var)
                board_state.append(".")

        # check if any move will win
        ret = self.check_win_move(available_spaces, board_state, size, symbol)
        if ret != 0xFF:
            return ret

        # block a win
        other_symbol = self.get_other_symbol(symbol)
        ret = self.check_win_move(available_spaces, board_state, size, other_symbol)
        if ret != 0xFF:
            return ret

        # check if a corner is free
        corners = [0, (size - 1), (size * (size - 1)), ((size * size) - 1)]
        open_corners = [x for x in available_spaces if x in corners]
        if len(open_corners) != 0:
            return random.choice(open_corners)

        # check if the middle is free
        middle = int((size * size) / 2)
        if middle in available_spaces:
            return middle

        return random.choice(available_spaces)

    @staticmethod
    def convert_position_to_row_and_col(element, size):
        col = 0
        row = 0
        for var in range(size):
            if element < (size * (var + 1)) and (element >= (size * var)):
                col = element - (size * var)
                row = var

        return [col, row]

    def get_move(self, board, symbol):
        size = board.size
        board_state = f"{board}".splitlines()
        board_state = "".join(board_state)

        element = self.get_position(board_state, symbol, size)

        move = self.convert_position_to_row_and_col(element, size)
        return [move[0], move[1]]
