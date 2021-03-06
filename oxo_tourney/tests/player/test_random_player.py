from unittest import TestCase
from unittest.mock import MagicMock

from hamcrest import assert_that, equal_to
from oxo_tourney.player import RandomPlayer


class TestRandomPlayer(TestCase):
    def test_name_returns_value_passed_into_constructor(self):
        player = RandomPlayer("some name")

        assert_that(player.name, equal_to("some name"))

    def test_next_move_returns_col_less_than_board_size(self):
        player = RandomPlayer("")
        board_mock = MagicMock()
        board_mock.size = 2
        max_col = 0
        for i in range(1000):
            col = player.get_move(board_mock)[0]
            if col > max_col:
                max_col = col
        assert_that(max_col, equal_to(1))

    def test_next_move_returns_row_less_than_board_size(self):
        player = RandomPlayer("")
        board_mock = MagicMock()
        board_mock.size = 2
        max_row = 0
        for i in range(1000):
            row = player.get_move(board_mock)[1]
            if row > max_row:
                max_row = row
        assert_that(max_row, equal_to(1))
