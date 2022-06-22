from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_move(self, board):
        """
        Get the next move to make

        :param board: string representing the current board state
        :return: list with column, row of next move
        """
