from oxo_tourney.player import ExamplePlayer
from oxo_tourney.tourney import Tourney


def main():
    player_list = [
        ExamplePlayer("1"),
        ExamplePlayer("2"),
        ExamplePlayer("3"),
        ExamplePlayer("4"),
    ]

    tourney = Tourney(player_list)
    summary, matrix = tourney.start()

    show_summary(summary)
    show_matrix(matrix, player_list)


def show_summary(summary):
    print("Results summary per player")
    print(f"{'Player':12}{'Wins':8}{'Losses':8}{'Draws':8}")
    for result in summary:
        print(f"{result[0]:12}{str(result[1]):8}{str(result[2]):8}{str(result[3]):8}")

    print()


def show_matrix(matrix, player_list):
    print("Results matrix")
    show_opponents(player_list)
    show_player_results(matrix)


def show_opponents(player_list):
    opponents = f"{'':12}"
    for player in player_list:
        opponents += f"{player.name:12} "
    print(opponents)


def show_player_results(matrix):
    for player in matrix:
        result_line = f"{player[0]:12}"
        for values in player[1]:
            scores = ",".join([str(i) for i in values])
            result_line += f"{scores:12} "
        print(result_line)


if __name__ == "__main__":
    main()
