from oxo_tourney.player.player import Player

# Create new player class from this template
# Add a line for your player class to the __init__.py file
# Implement your version of the get_move function


class ExamplePlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board="", symbol=""):
        # Only ever chooses the same move, can't be used to play a complete game
        return [0, 0]
