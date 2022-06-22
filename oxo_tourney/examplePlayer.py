from oxo_tourney.player import Player


class ExamplePlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board):
        pass
