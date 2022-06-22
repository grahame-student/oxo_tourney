from unittest import TestCase

from hamcrest import assert_that, equal_to
from oxo_tourney.player import ExamplePlayer


class TestExamplePlayer(TestCase):
    def test_name_returns_value_passed_into_constructor(self):
        player = ExamplePlayer("some name")

        assert_that(player.name, equal_to("some name"))

    def test_get_next_move_returns_row_and_column(self):
        player = ExamplePlayer("some name")
        move = player.get_move("")
        assert_that(move, equal_to([0, 0]))
