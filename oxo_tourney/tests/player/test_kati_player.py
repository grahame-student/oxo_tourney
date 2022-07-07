from unittest import TestCase
from unittest.mock import MagicMock

from hamcrest import any_of, assert_that, equal_to, is_not, less_than
from oxo_tourney.player import BraveBraveSirRobinPlayer
from oxo_tourney.constants import *


class TestBraveBraveSirRobin(TestCase):
    def test_name_returns_value_passed_into_constructor(self):
        player = BraveBraveSirRobinPlayer("some name")

        assert_that(player.name, equal_to("some name"))

    def test_next_move_returns_col_less_than_board_size(self):
        player = BraveBraveSirRobinPlayer("")
        board_mock = MagicMock()
        board_mock.size = 3
        max_col = 0
        for i in range(1000):
            col = player.get_move(board_mock, PLAYER_2)
            if col[0] > max_col:
                max_col = col[0]
        assert_that(max_col, less_than(3))

    def test_next_move_returns_row_less_than_board_size(self):
        player = BraveBraveSirRobinPlayer("")
        board_mock = MagicMock()
        board_mock.size = 2
        max_row = 0
        for i in range(1000):
            row = player.get_move(board_mock, PLAYER_2)
            if row[1] > max_row:
                max_row = row[1]
        assert_that(max_row, less_than(2))

    def test_check_rows_returns_win(self):
        player = BraveBraveSirRobinPlayer("")
        board_mock = [PLAYER_2, PLAYER_2, ".", "."]
        result = player.check_rows(board_mock, PLAYER_2, 2)
        assert_that(result, equal_to(1))

    def test_check_rows_returns_fail(self):
        player = BraveBraveSirRobinPlayer("")
        board_mock = [PLAYER_2, PLAYER_1, ".", "."]
        result = player.check_rows(board_mock, PLAYER_2, 2)
        assert_that(result, equal_to(0))

    def test_check_columns_returns_win(self):
        player = BraveBraveSirRobinPlayer("")
        board_mock = [PLAYER_2, ".", PLAYER_2, "."]
        result = player.check_columns(board_mock, PLAYER_2, 2)
        assert_that(result, equal_to(2))

    def test_check_columns_returns_fail(self):
        player = BraveBraveSirRobinPlayer("")
        board_mock = [PLAYER_2, PLAYER_1, ".", "."]
        result = player.check_columns(board_mock, PLAYER_2, 2)
        assert_that(result, equal_to(0))

    def test_check_diagonal_forward_returns_win(self):
        player = BraveBraveSirRobinPlayer("")
        board_mock = [PLAYER_2, ".", PLAYER_1, ".", PLAYER_2, ".", PLAYER_1, PLAYER_1, PLAYER_2]
        result = player.check_diagonals(board_mock, PLAYER_2, 3)
        assert_that(result, equal_to(3))

    def test_check_diagonal_backwards_returns_win(self):
        player = BraveBraveSirRobinPlayer("")
        board_mock = [PLAYER_2, ".", PLAYER_1, ".", PLAYER_1, ".", PLAYER_1, PLAYER_1, "."]
        result = player.check_diagonals(board_mock, PLAYER_1, 3)
        assert_that(result, equal_to(4))

    def test_check_diagonal_returns_fail(self):
        player = BraveBraveSirRobinPlayer("")
        board_mock = [PLAYER_2, ".", PLAYER_1, ".", PLAYER_2, ".", PLAYER_1, PLAYER_1, "."]
        result = player.check_diagonals(board_mock, PLAYER_1, 3)
        assert_that(result, equal_to(0))

    def test_other_symbol_returns_O(self):
        player = BraveBraveSirRobinPlayer("")
        symbol = PLAYER_2
        result = player.get_other_symbol(symbol)
        assert_that(result, equal_to(PLAYER_1))

    def test_other_symbol_returns_X(self):
        player = BraveBraveSirRobinPlayer("")
        symbol = PLAYER_1
        result = player.get_other_symbol(symbol)
        assert_that(result, equal_to(PLAYER_2))

    def test_other_symbol_returns_blank(self):
        player = BraveBraveSirRobinPlayer("")
        symbol = "A"
        result = player.get_other_symbol(symbol)
        assert_that(result, equal_to("."))

    def test_get_position_returns_win_space(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 9
        board[0] = PLAYER_2
        board[1] = PLAYER_2
        result = player.get_position(board, PLAYER_2, 3)
        assert_that(result, equal_to(2))

    def test_get_position_returns_block_space(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 9
        board[0] = PLAYER_1
        board[1] = PLAYER_1
        result = player.get_position(board, PLAYER_2, 3)
        assert_that(result, equal_to(2))

    def test_get_position_returns_middle_space(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 25
        board[0] = PLAYER_2
        board[4] = PLAYER_2
        board[20] = PLAYER_1
        board[24] = PLAYER_2
        result = player.get_position(board, PLAYER_1, 5)
        assert_that(result, equal_to(12))

    def test_get_position_returns_corner(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 25
        result = player.get_position(board, PLAYER_1, 5)
        assert_that(result, any_of(0, 4, 20, 24))

    def test_find_better_move_diagonal_backwards_returns_space(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 25
        board[0] = PLAYER_1
        board[4] = PLAYER_2
        board[12] = PLAYER_2
        board[20] = PLAYER_2
        board[24] = PLAYER_1
        result = player.get_position(board, PLAYER_1, 5)
        assert_that(result, any_of(8, 16))

    def test_find_better_move_diagonal_forwards_returns_space(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 25
        board[0] = PLAYER_1
        board[4] = PLAYER_2
        board[12] = PLAYER_1
        board[20] = PLAYER_2
        board[24] = PLAYER_1
        result = player.get_position(board, PLAYER_2, 5)
        assert_that(result, any_of(6, 18))

    def test_find_better_move_columns_returns_space(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 25
        board[0] = PLAYER_1
        board[4] = PLAYER_2
        board[12] = PLAYER_1
        board[20] = PLAYER_2
        board[24] = PLAYER_2
        result = player.get_position(board, PLAYER_1, 5)
        assert_that(result, any_of(9, 14, 19))

    def test_find_better_move_rows_returns_space(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 25
        board[0] = PLAYER_1
        board[2] = PLAYER_1
        board[4] = PLAYER_2
        board[10] = PLAYER_2
        board[12] = PLAYER_2
        board[20] = PLAYER_1
        board[22] = PLAYER_2
        board[24] = PLAYER_1
        result = player.get_position(board, PLAYER_1, 5)
        assert_that(result, any_of(11, 13, 14))

    def test_find_better_move_columns_returns_block(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 25
        board[0] = PLAYER_1
        board[4] = PLAYER_2
        board[5] = PLAYER_1
        board[6] = PLAYER_2
        board[12] = PLAYER_1
        board[13] = PLAYER_2
        board[18] = PLAYER_2
        board[19] = PLAYER_1
        board[20] = PLAYER_2
        board[24] = PLAYER_1
        result = player.get_position(board, PLAYER_1, 5)
        assert_that(result, any_of(3, 8, 23))

    def test_find_better_move_columns_returns_space(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 25
        board[0] = PLAYER_1
        board[4] = PLAYER_2
        board[5] = PLAYER_1
        board[6] = PLAYER_2
        board[12] = PLAYER_1
        board[13] = PLAYER_2
        board[16] = PLAYER_1
        board[18] = PLAYER_2
        board[19] = PLAYER_1
        board[20] = PLAYER_2
        board[22] = PLAYER_1
        board[23] = PLAYER_1
        board[24] = PLAYER_1
        result = player.get_position(board, PLAYER_1, 5)
        assert_that(result, any_of(2, 7, 17))

    def test_find_better_move_columns_returns_space(self):
        player = BraveBraveSirRobinPlayer("")
        board = ["."] * 25
        board[0] = PLAYER_1
        board[4] = PLAYER_2
        board[5] = PLAYER_1
        board[6] = PLAYER_2
        board[12] = PLAYER_1
        board[13] = PLAYER_2
        board[16] = PLAYER_1
        board[18] = PLAYER_2
        board[19] = PLAYER_1
        board[20] = PLAYER_2
        board[22] = PLAYER_2
        board[23] = PLAYER_1
        board[24] = PLAYER_1
        result = player.get_position(board, PLAYER_1, 5)
        assert_that(result, any_of(1, 2, 3, 7, 8, 9, 10, 11, 14, 15, 17, 21))
