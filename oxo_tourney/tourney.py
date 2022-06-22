from oxo_tourney.examplePlayer import ExamplePlayer


class Tourney:
    def __init__(self):
        self.__players = [
            ExamplePlayer("1"),
            ExamplePlayer("2"),
            ExamplePlayer("3"),
            ExamplePlayer("4"),
        ]

    def start(self):
        for player1 in self.__players:
            for player2 in self.__players:
                if player1 == player2:
                    continue
                print(f"{player1.name} vs {player2.name}")
