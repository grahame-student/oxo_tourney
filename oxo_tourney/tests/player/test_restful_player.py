from unittest import TestCase

from hamcrest import assert_that, equal_to
from oxo_tourney.player import RestfulPlayer


class TestRestfulPlayer(TestCase):
    def test_name_returns_value_passed_into_constructor(self):
        player = RestfulPlayer("some name")

        assert_that(player.name, equal_to("some name"))
