from unittest import TestCase, mock

from hamcrest import assert_that, equal_to
from oxo_tourney import constants
from oxo_tourney.player import HumanPlayer
from oxo_tourney.tourney import Tourney

player_1_win = [
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

player_2_win = [
    2,
    0,  # p1
    0,
    0,  # p2
    1,
    0,  # p1
    1,
    1,  # p2
    0,
    2,  # p1
    2,
    2,  # p2 win
]

draw = [
    0,
    0,
    1,
    0,
    2,
    0,
    0,
    2,
    1,
    2,
    2,
    2,
    0,
    1,
    1,
    1,
    2,
    1,
]


class TestTourney(TestCase):
    def test_start_returns_2_results_when_2_players_passed_in(self):
        with mock.patch("builtins.input", side_effect=player_1_win + player_1_win):
            player_list = [HumanPlayer(""), HumanPlayer("")]
            tourney = Tourney(player_list)
            tourney.start()

        assert_that(len(tourney.score_matrix), equal_to(2))

    def test_score_matrix_has_2_wins_for_player_1_vs_player_2(self):
        with mock.patch("builtins.input", side_effect=player_1_win + player_2_win):
            player_list = [HumanPlayer(""), HumanPlayer("")]
            tourney = Tourney(player_list)
            tourney.start()

        player_1_score = tourney.score_matrix[player_list[0].id][player_list[1].id][
            constants.SCORE_WINS
        ]

        assert_that(player_1_score, equal_to(2))

    def test_score_matrix_has_2_wins_for_player_2_vs_player_1(self):
        with mock.patch("builtins.input", side_effect=player_2_win + player_1_win):
            player_list = [HumanPlayer(""), HumanPlayer("")]
            tourney = Tourney(player_list)
            tourney.start()
            print(tourney.score_matrix)

        player_2_score = tourney.score_matrix[player_list[1].id][player_list[0].id][
            constants.SCORE_WINS
        ]

        assert_that(player_2_score, equal_to(2))

    def test_score_matrix_has_2_losses_for_player_1_vs_player_2(self):
        with mock.patch("builtins.input", side_effect=player_2_win + player_1_win):
            player_list = [HumanPlayer(""), HumanPlayer("")]
            tourney = Tourney(player_list)
            tourney.start()

        player_1_score = tourney.score_matrix[player_list[0].id][player_list[1].id][
            constants.SCORE_LOSSES
        ]

        assert_that(player_1_score, equal_to(2))

    def test_score_matrix_has_2_losses_for_player_2_vs_player_1(self):
        with mock.patch("builtins.input", side_effect=player_1_win + player_2_win):
            player_list = [HumanPlayer(""), HumanPlayer("")]
            tourney = Tourney(player_list)
            tourney.start()
            print(tourney.score_matrix)

        player_2_score = tourney.score_matrix[player_list[1].id][player_list[0].id][
            constants.SCORE_LOSSES
        ]

        assert_that(player_2_score, equal_to(2))

    def test_score_matrix_has_2_draws_for_player_1_vs_player_2(self):
        with mock.patch("builtins.input", side_effect=draw + draw):
            player_list = [HumanPlayer(""), HumanPlayer("")]
            tourney = Tourney(player_list)
            tourney.start()

        player_1_score = tourney.score_matrix[player_list[0].id][player_list[1].id][
            constants.SCORE_DRAWS
        ]

        assert_that(player_1_score, equal_to(2))

    def test_score_matrix_has_2_draws_for_player_2_vs_player_1(self):
        with mock.patch("builtins.input", side_effect=draw + draw):
            player_list = [HumanPlayer(""), HumanPlayer("")]
            tourney = Tourney(player_list)
            tourney.start()
            print(tourney.score_matrix)

        player_2_score = tourney.score_matrix[player_list[1].id][player_list[0].id][
            constants.SCORE_DRAWS
        ]

        assert_that(player_2_score, equal_to(2))
