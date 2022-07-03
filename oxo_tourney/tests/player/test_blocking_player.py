from unittest import TestCase
from unittest.mock import MagicMock

from hamcrest import assert_that, equal_to
from oxo_tourney.player import BlockingPlayer


class TestExamplePlayer(TestCase):
    def test_name_returns_value_passed_into_constructor(self):
        player = BlockingPlayer("some name")

        assert_that(player.name, equal_to("some name"))

    def test_get_next_move_returns_row_and_column(self):
        player = BlockingPlayer("some name")

        board_mock = MagicMock()
        board_mock.size = 3
        board_mock.__str__.return_value = "...\n...\n..."

        move = player.get_move(board_mock, "X")
        assert_that(len(move), equal_to(2))

    def test_get_move_selects_centre_square_when_board_empty(self):
        player = BlockingPlayer("some name")

        board_mock = MagicMock()
        board_mock.size = 3
        board_mock.__str__.return_value = "...\n...\n..."

        move = player.get_move(board_mock, "X")
        assert_that(move, equal_to([1, 1]))

    def test_get_move_selects_corner_cell_when_center_of_board_taken(self):
        player = BlockingPlayer("some name")

        board_mock = MagicMock()
        board_mock.size = 3
        board_mock.__str__.return_value = "...\n.O.\n..."

        move = player.get_move(board_mock, "X")
        assert_that(move, equal_to([0, 0]))
