import uuid
from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, name):
        # uuid allows each individual player to be tracked even if they have the same name
        self.id = str(uuid.uuid4().hex)
        self.name = name
        # Wins, Losses, Draws
        self.score_summary = [0, 0, 0]

    @abstractmethod
    def get_move(self, board, symbol):
        """
        Get the next move to make

        :param symbol: Symbol used by the current player
        :param board: string representing the current board state
        :return: list with column, row of next move
        """
