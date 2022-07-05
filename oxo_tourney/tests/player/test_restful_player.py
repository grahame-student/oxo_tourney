from unittest import TestCase
from unittest.mock import MagicMock

from hamcrest import assert_that, equal_to
from oxo_tourney.player import RestfulPlayer


class TestRestfulPlayer(TestCase):
    def test_name_returns_value_passed_into_constructor(self):
        player = RestfulPlayer("some name")

        assert_that(player.name, equal_to("some name"))

    def test_move_contains_two_elements(self):
        # Not a good test case!
        player = RestfulPlayer("")
        board_mock = MagicMock()
        board_mock.size = 2
        board_mock.__str__.return_value = "...\n...\n..."

        move = player.get_move(board_mock, "X")

        assert_that(len(move), equal_to(2))
