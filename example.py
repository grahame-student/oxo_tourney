from oxo_tourney.tourney import Tourney
from oxo_tourney.player import ExamplePlayer


def main():
    player_list = [
        ExamplePlayer("1"),
        ExamplePlayer("2"),
        ExamplePlayer("3"),
        ExamplePlayer("4"),
    ]

    tourney = Tourney(player_list)
    tourney.start()


if __name__ == "__main__":
    main()
