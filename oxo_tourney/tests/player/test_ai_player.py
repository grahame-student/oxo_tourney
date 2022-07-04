from unittest import TestCase
from unittest.mock import MagicMock
from hamcrest import assert_that, equal_to
from oxo_tourney.player import AiPlayer


class TestAiPlayer(TestCase):
    def test_name_returns_value_passed_into_constructor(self):
        player = AiPlayer("some name")

        assert_that(player.name, equal_to("some name"))

    def test_get_move_returns_a_list_with_two_elements(self):
        player = AiPlayer("some name")
        board_mock = MagicMock()
        board_mock.size = 2
        board_mock.__str__.return_value = "...\n...\n..."

        move = player.get_move(board_mock, "X")

        assert_that(len(move), equal_to(2))

    def test_get_move_returns_empty_list_when_board_is_full(self):
        player = AiPlayer("some name")
        board_mock = MagicMock()
        board_mock.size = 2
        board_mock.__str__.return_value = "XOX\nOXX\nOXO"

        move = player.get_move(board_mock, "X")

        assert_that(len(move), equal_to(0))
