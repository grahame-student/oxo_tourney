import random

from oxo_tourney.constants import *
from oxo_tourney.player.player import Player


class BraveBraveSirRobinPlayer(Player):
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
    def check_rows_for_line(board, symbol, size):
        return_value = 0
        count = 0
        for var in range(size):
            for ret in range(size):
                if board[ret + (size * var)] == symbol:
                    count += 1
                else:
                    count = 0
                if count == size:
                    return_value = 1
        return return_value

    @staticmethod
    def check_rows_for_contents(board, symbol, size):
        count = [] * size
        for var in range(size):
            for ret in range(size):
                if board[ret + (size * var)] == symbol:
                    count[var] += 1
                elif board[ret + (size * var)] != ".":
                    count = 0
        for var in range(size):
            if count[var] == max(count):
                return count[var]

    @staticmethod
    def check_columns_for_line(board, symbol, size):
        count = 0
        return_value = 0
        for var in range(size):
            for ret in range(size):
                if board[var + (size * ret)] == symbol:
                    count += 1
                else:
                    count = 0
                if count == size:
                    return_value = 2
        return return_value

    @staticmethod
    def check_col_for_contents(board, symbol, size):
        count = [0] * size
        for var in range(size):
            for ret in range(size):
                if board[var + (size * ret)] == symbol:
                    count[var] += 1
                elif board[var + (size * ret)] != ".":
                    count = 0
        for var in range(size):
            if count[var] == max(count):
                return count[var]

    @staticmethod
    def check_diagonals_for_line(board, symbol, size):
        count = 0
        return_value = 0
        # forwards
        for var in range(size):
            if board[((size + 1) * var)] == symbol:
                count += 1
            else:
                count = 0
            if count == size:
                return_value = 3

        count = 0
        # backwards
        for var in range(size):
            if board[(size - 1) * (var + 1)] == symbol:
                count += 1
            else:
                count = 0
            if count == size:
                return_value = 4

        return return_value

    @staticmethod
    def check_diagonal_forward_for_contents(board, symbol, size):
        count = 0
        return_value = 0
        # forwards
        for var in range(size):
            if board[((size + 1) * var)] == symbol:
                count += 1
            elif board[((size + 1) * var)] != ".":
                count = 0
        if count != 0:
            return_value = 5
        return return_value

    @staticmethod
    def check_diagonal_backwards_for_contents(board, symbol, size):
        count = 0
        return_value = 0
        # backwards
        for var in range(size):
            if board[(size - 1) * (var + 1)] == symbol:
                count += 1
            elif board[(size - 1) * (var + 1)] == symbol:
                count = 0
        if count != 0:
            return_value = 6
        return return_value

    @staticmethod
    def check_win_board(board, symbol, size):
        return_value: int = 0
        return_value += BraveBraveSirRobinPlayer.check_rows_for_line(board, symbol, size)
        return_value += BraveBraveSirRobinPlayer.check_columns_for_line(board, symbol, size)
        return_value += BraveBraveSirRobinPlayer.check_diagonals_for_line(board, symbol, size)
        return return_value

    @staticmethod
    def check_win_move(spaces, board, size, symbol):
        for var in spaces:
            board_copy = board
            board_copy[var] = symbol
            temp = BraveBraveSirRobinPlayer.check_win_board(board_copy, symbol, size)
            board_copy[var] = "."
            if temp != 0:
                ret = var
                return ret
        return 0xFF

    @staticmethod
    def check_next_best_move(spaces, board, size, symbol):
        # todo fix this - spaces isn't the correct thing to check,
        #  need ot check the elements in the diagonal/row/col not the available spaces
        for var in spaces:
            if BraveBraveSirRobinPlayer.check_diagonal_forward_for_contents(board, symbol, size) != 0:
                return var
            elif BraveBraveSirRobinPlayer.check_diagonal_backwards_for_contents(board, symbol, size) != 0:
                return var
            # elif BraveBraveSirRobinPlayer.check_rows_for_contents(board, symbol, size) != 0:
            #     return var
            # elif BraveBraveSirRobinPlayer.check_col_for_contents(board, symbol, size) != 0:
            #     return var
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
        ret = BraveBraveSirRobinPlayer.check_win_move(available_spaces, board_state, size, symbol)
        if ret != 0xFF:
            return ret

        # block a win
        other_symbol = self.get_other_symbol(symbol)
        ret = BraveBraveSirRobinPlayer.check_win_move(available_spaces, board_state, size, other_symbol)
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

        # Check if diagonal/row/col has only their symbol - if yes, go there
        print("kw1")
        ret = BraveBraveSirRobinPlayer.check_next_best_move(available_spaces, board_state, size, other_symbol)
        if ret != 0xFF:
            return ret
        print("kw2")
        # Check if diagonal/row/col has only my symbol - if yes, go there
        ret = BraveBraveSirRobinPlayer.check_next_best_move(available_spaces, board_state, size, symbol)
        if ret != 0xFF:
            return ret
        print("kw3")
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

        move = BraveBraveSirRobinPlayer.convert_position_to_row_and_col(element, size)
        return [move[0], move[1]]
