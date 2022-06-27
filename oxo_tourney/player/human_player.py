from oxo_tourney.player.player import Player


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board=None, symbol=""):
        print(f"{self.name}'s turn to move")
        col = int(input("Enter col"))
        row = int(input("Enter row"))
        return [col, row]
