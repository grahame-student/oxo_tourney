from typing import List, Union

from oxo_tourney.board import Board
from oxo_tourney.player.player import Player


class BlockingPlayer(Player):
    # Max score includes row, col and both diagonals
    MAX_SCORE = 4

    def __init__(self, name):
        super().__init__(name)
        self.__grid: Union[List[str], None] = None
        self.__symbol: Union[str, None] = None

    def get_move(self, board: Board, symbol: str) -> List[int]:
        # Player goal - Make the board unwinnable for the opposition
        self.__grid = str(board).splitlines()
        self.__symbol = symbol

        max_score = -1
        result = []
        for row in range(board.size):
            for col in range(board.size):
                score = self.__get_cell_score(row, col)
                if score > max_score:
                    result = [col, row]
                    max_score = score
                if max_score == BlockingPlayer.MAX_SCORE:
                    break
            if max_score == BlockingPlayer.MAX_SCORE:
                break
        return result

    def __get_cell_score(self, row: int, col: int) -> int:
        result = 0
        cell = self.__grid[row][col]
        if cell == ".":
            if self.__can_make_row(row):
                result += 1
            if self.__can_make_col(col):
                result += 1
            if self.__is_diagonal(row, col, True) and self.__can_make_diagonal(True):
                result += 1
            if self.__is_diagonal(row, col, False) and self.__can_make_diagonal(False):
                result += 1
        else:
            result = -1
        return result

    def __can_make_row(self, row: int) -> bool:
        """
        Return False if player has played in this row
        :param row:
        :return:
        """
        return self.__grid[row].find(self.__symbol) == -1

    def __can_make_col(self, col: int):
        """
        Return False if player has played in this col
        :param col:
        :return:
        """
        string: str = ""
        for row in self.__grid:
            string += row[col]
        return string.find(self.__symbol) == -1

    def __is_diagonal(self, col: int, row: int, is_dr) -> bool:
        return (row == col) if is_dr else row == (self.__get_max_col() - col)

    def __get_max_col(self) -> int:
        max_col: int = len(self.__grid[0]) - 1
        return max_col

    def __can_make_diagonal(self, is_dr) -> bool:
        """
        Return False if player has played in a diagonal
        :return:
        """
        string: str = ""
        max_col = self.__get_max_col()
        for i in range(len(self.__grid[0])):
            string += self.__grid[i][i] if is_dr else self.__grid[i][max_col - i]
        return string.find(self.__symbol) == -1
