from unittest import TestCase, mock

from hamcrest import assert_that, equal_to
from oxo_tourney import constants
from oxo_tourney.game import Game
from oxo_tourney.player import HumanPlayer

complete_game_input = [
    0,
    0,  # p1
    0,
    0,  # p2 - invalid
    0,
    1,  # p2
    1,
    1,  # p1
    1,
    0,  # p2
    2,
    2,  # p1 win
]


class TestGame(TestCase):
    def test_game_prompts_for_new_input_when_previously_selected_cell_entered(self):
        # Not a great test, the assertion doesn't check what the test states it is for
        with mock.patch(
            "builtins.input", side_effect=complete_game_input + complete_game_input
        ):
            player_list = [HumanPlayer(""), HumanPlayer("")]
            game = Game(player_list[0], player_list[1], 3)
            result = game.start()

        assert_that(result[1], equal_to(constants.PLAYER_1))
