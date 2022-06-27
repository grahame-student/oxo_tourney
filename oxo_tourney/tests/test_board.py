from unittest import TestCase

from hamcrest import assert_that, equal_to
from oxo_tourney import constants
from oxo_tourney.board import Board


class TestBoard(TestCase):
    def test_constructor_creates_board_with_size_rows(self):
        board = Board(5)
        grid = str(board)
        assert_that(grid.count("\n"), equal_to(5))

    def test_constructor_creates_board_with_size_columns(self):
        board = Board(5)
        grid = str(board).splitlines()
        assert_that(len(grid[0]), equal_to(5))

    def test_valid_move_returns_true_when_cell_empty(self):
        board = Board(5)
        assert_that(board.valid_move(0, 0), equal_to(True))

    def test_valid_move_returns_false_when_cell_full(self):
        board = Board(5)
        board.set_cell(0, 0, "X")
        assert_that(board.valid_move(0, 0), equal_to(False))

    def test_state_returns_in_progress_when_no_winner(self):
        board = Board(5)
        assert_that(board.state, equal_to(constants.STATE_IN_PROGRESS))

    def test_state_returns_win_when_horizontal_line_completed(self):
        board = Board(3)
        board.set_cell(0, 0, "X")
        board.set_cell(1, 0, "X")
        board.set_cell(2, 0, "X")
        assert_that(board.state, equal_to(constants.STATE_WIN))

    def test_state_returns_win_when_vertical_line_completed(self):
        board = Board(3)
        board.set_cell(0, 0, "X")
        board.set_cell(0, 1, "X")
        board.set_cell(0, 2, "X")
        assert_that(board.state, equal_to(constants.STATE_WIN))

    def test_state_returns_win_when_down_right_line_completed(self):
        board = Board(3)
        board.set_cell(0, 0, "X")
        board.set_cell(1, 1, "X")
        board.set_cell(2, 2, "X")
        assert_that(board.state, equal_to(constants.STATE_WIN))

    def test_state_returns_win_when_down_left_line_completed(self):
        board = Board(3)
        board.set_cell(0, 2, "X")
        board.set_cell(1, 1, "X")
        board.set_cell(2, 0, "X")
        assert_that(board.state, equal_to(constants.STATE_WIN))

    def test_state_returns_draw_when_board_full_and_no_lines_completed(self):
        board = Board(3)
        board.set_cell(0, 0, "a")
        board.set_cell(0, 1, "b")
        board.set_cell(0, 2, "c")
        board.set_cell(1, 0, "d")
        board.set_cell(1, 1, "e")
        board.set_cell(1, 2, "f")
        board.set_cell(2, 0, "g")
        board.set_cell(2, 1, "h")
        board.set_cell(2, 2, "i")
        assert_that(board.state, equal_to(constants.STATE_DRAW))

    def test_winner_returns_None_when_board_full_and_no_lines_completed(self):
        board = Board(3)
        board.set_cell(0, 0, "z")
        board.set_cell(0, 1, "y")
        board.set_cell(0, 2, "x")
        board.set_cell(1, 0, "w")
        board.set_cell(1, 1, "v")
        board.set_cell(1, 2, "u")
        board.set_cell(2, 0, "t")
        board.set_cell(2, 1, "s")
        board.set_cell(2, 2, "r")
        assert_that(board.winner, equal_to(None))

    def test_winner_returns_winning_player_when_line_completed(self):
        board = Board(3)
        board.set_cell(0, 0, "X")
        board.set_cell(1, 0, "X")
        board.set_cell(2, 0, "X")
        assert_that(board.winner, equal_to(constants.PLAYER_2))
