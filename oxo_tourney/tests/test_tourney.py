from unittest import TestCase, mock

from hamcrest import assert_that, equal_to
from oxo_tourney.player import HumanPlayer
from oxo_tourney.tourney import Tourney

complete_game_input = [
    0,
    0,  # p1
    0,
    1,  # p2
    1,
    1,  # p1
    1,
    0,  # p2
    2,
    2,  # p1 win
]


class TestTourney(TestCase):
    def test_start_returns_2_results_when_2_players_passed_in(self):
        with mock.patch(
            "builtins.input", side_effect=complete_game_input + complete_game_input
        ):
            player_list = [HumanPlayer(""), HumanPlayer("")]
            tourney = Tourney(player_list)
            tourney.start()

        assert_that(len(tourney.score_matrix), equal_to(2))
