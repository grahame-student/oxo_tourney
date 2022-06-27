from unittest import TestCase, mock

from hamcrest import assert_that, equal_to
from oxo_tourney.player import HumanPlayer


class TestExamplePlayer(TestCase):
    def test_name_returns_value_passed_into_constructor(self):
        player = HumanPlayer("some name")

        assert_that(player.name, equal_to("some name"))

    def test_get_next_move_returns_row_and_column(self):
        with mock.patch("builtins.input", side_effect=[1, 2]):
            player = HumanPlayer("some name")
            move = player.get_move("")
            assert_that(move, equal_to([1, 2]))
