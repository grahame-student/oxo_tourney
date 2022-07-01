from unittest import TestCase
from unittest.mock import MagicMock

from hamcrest import assert_that, equal_to, is_not, less_than
from oxo_tourney.player import KatiPlayer


class TestKatiPlayer(TestCase):
    def test_name_returns_value_passed_into_constructor(self):
        player = KatiPlayer("some name")

        assert_that(player.name, equal_to("some name"))

    def test_next_move_returns_col_less_than_board_size(self):
        player = KatiPlayer("")
        board_mock = MagicMock()
        board_mock.size = 3
        max_col = 0
        for i in range(1000):
            col = player.get_move(board_mock, "X")
            if col[0] > max_col:
                max_col = col[0]
        assert_that(max_col, less_than(3))

    def test_next_move_returns_row_less_than_board_size(self):
        player = KatiPlayer("")
        board_mock = MagicMock()
        board_mock.size = 2
        max_row = 0
        for i in range(1000):
            row = player.get_move(board_mock, "X")
            if row[1] > max_row:
                max_row = row[1]
        assert_that(max_row, less_than(2))

    def test_check_rows_returns_win(self):
        player = KatiPlayer("")
        board_mock = ["X", "X", ".", "."]
        result = player.check_rows(board_mock, "X", 2)
        assert_that(result, equal_to(1))

    def test_check_rows_returns_fail(self):
        player = KatiPlayer("")
        board_mock = ["X", "O", ".", "."]
        result = player.check_rows(board_mock, "X", 2)
        assert_that(result, equal_to(0))

    def test_check_columns_returns_win(self):
        player = KatiPlayer("")
        board_mock = ["X", ".", "X", "."]
        result = player.check_columns(board_mock, "X", 2)
        assert_that(result, equal_to(2))

    def test_check_columns_returns_fail(self):
        player = KatiPlayer("")
        board_mock = ["X", "O", ".", "."]
        result = player.check_columns(board_mock, "X", 2)
        assert_that(result, equal_to(0))

    def test_check_diagonal_forward_returns_win(self):
        player = KatiPlayer("")
        board_mock = ["X", ".", "O", ".", "X", ".", "O", "O", "X"]
        result = player.check_diagonals(board_mock, "X", 3)
        assert_that(result, equal_to(3))

    def test_check_diagonal_backwards_returns_win(self):
        player = KatiPlayer("")
        board_mock = ["X", ".", "O", ".", "O", ".", "O", "O", "."]
        result = player.check_diagonals(board_mock, "O", 3)
        assert_that(result, equal_to(4))

    def test_check_diagonal_returns_fail(self):
        player = KatiPlayer("")
        board_mock = ["X", ".", "O", ".", "X", ".", "O", "O", "."]
        result = player.check_diagonals(board_mock, "O", 3)
        assert_that(result, equal_to(0))

    def test_other_symbol_returns_O(self):
        player = KatiPlayer("")
        symbol = "X"
        result = player.get_other_symbol(symbol)
        assert_that(result, equal_to("O"))

    def test_other_symbol_returns_X(self):
        player = KatiPlayer("")
        symbol = "O"
        result = player.get_other_symbol(symbol)
        assert_that(result, equal_to("X"))

    def test_other_symbol_returns_blank(self):
        player = KatiPlayer("")
        symbol = "A"
        result = player.get_other_symbol(symbol)
        assert_that(result, equal_to("."))

    def test_get_position_returns_win_space(self):
        player = KatiPlayer("")
        board = ["."] * 9
        board[0] = "X"
        board[1] = "X"
        result = player.get_position(board, "X", 3)
        assert_that(result, equal_to(2))

    def test_get_position_returns_block_space(self):
        player = KatiPlayer("")
        board = ["."] * 9
        board[0] = "O"
        board[1] = "O"
        result = player.get_position(board, "X", 3)
        assert_that(result, equal_to(2))

    def test_get_position_returns_middle_space(self):
        player = KatiPlayer("")
        board = ["."] * 25
        board[0] = "X"
        board[4] = "X"
        board[20] = "O"
        board[24] = "X"
        result = player.get_position(board, "O", 5)
        assert_that(result, equal_to(12))

    def test_get_position_returns_random_space(self):
        player = KatiPlayer("")
        board = ["."] * 25
        board[0] = "X"
        board[4] = "X"
        board[20] = "O"
        board[24] = "X"
        board[12] = "O"
        result = player.get_position(board, "O", 5)
        assert_that(result, is_not(0 or 4 or 12 or 20 or 24))
