from unittest import TestCase
from unittest.mock import MagicMock

from hamcrest import *  # assert_that, equal_to
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
            if col > max_col:
                max_col = col
        assert_that(max_col, less_than(3))

    def test_next_move_returns_row_less_than_board_size(self):
        player = KatiPlayer("")
        board_mock = MagicMock()
        board_mock.size = 2
        max_row = 0
        for i in range(1000):
            row = player.get_move(board_mock, "X")
            if row > max_row:
                max_row = row
        assert_that(max_row, less_than(2))

    def test_check_rows_returns_win(self):
        player = KatiPlayer("")
        board_mock = ["X", "X", ".", "."]
        print("kw", board_mock)
        result = player.check_rows(board_mock, "X", 2)
        assert_that(result, equal_to(1))

    def test_check_rows_returns_fail(self):
        player = KatiPlayer("")
        board_mock = ["X", "O", ".", "."]
        print("kw", board_mock)
        result = player.check_rows(board_mock, "X", 2)
        assert_that(result, equal_to(0))

    def test_check_columns_returns_win(self):
        player = KatiPlayer("")
        board_mock = ["X", ".", "X", "."]
        print("kw", board_mock)
        result = player.check_columns(board_mock, "X", 2)
        assert_that(result, equal_to(2))

    def test_check_columns_returns_fail(self):
        player = KatiPlayer("")
        board_mock = ["X", "O", ".", "."]
        print("kw", board_mock)
        result = player.check_columns(board_mock, "X", 2)
        assert_that(result, equal_to(0))

    def test_check_diagonal_forward_returns_win(self):
        player = KatiPlayer("")
        board_mock = ["X", ".", "O", ".", "X", ".", "O", "O", "X"]
        print("kw", board_mock)
        result = player.check_diagonals(board_mock, "X", 3)
        assert_that(result, equal_to(3))

    def test_check_diagonal_backwards_returns_win(self):
        player = KatiPlayer("")
        board_mock = ["X", ".", "O", ".", "O", ".", "O", "O", "."]
        print("kw", board_mock)
        result = player.check_diagonals(board_mock, "O", 3)
        assert_that(result, equal_to(4))

    def test_check_diagonal_returns_fail(self):
        player = KatiPlayer("")
        board_mock = ["X", ".", "O", ".", "X", ".", "O", "O", "."]
        print("kw", board_mock)
        result = player.check_diagonals(board_mock, "O", 3)
        assert_that(result, equal_to(0))