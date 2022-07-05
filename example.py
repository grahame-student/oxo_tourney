from oxo_tourney import constants
from oxo_tourney.player import BraveBraveSirRobinPlayer, RandomPlayer, RestfulPlayer
from oxo_tourney.tourney import Tourney


def main():
    player_list = [
        RandomPlayer("Player 1"),
        RandomPlayer("Player 2"),
        RestfulPlayer("Player 3"),
        BraveBraveSirRobinPlayer("Player 4"),
    ]
    tourney = Tourney(player_list)
    tourney.start()

    show_summary(player_list)
    show_matrix(tourney.score_matrix, player_list)


def show_summary(player_list):
    print("Results summary per player")
    print(f"{'Player':12}{'Wins':8}{'Losses':8}{'Draws':8}")
    for player in player_list:
        summary_line = get_summary_line(player)
        print(summary_line)

    print()


def get_summary_line(player):
    return (
        f"{player.name:12}"
        + f"{str(player.score_summary[constants.SCORE_WINS]):8}"
        + f"{str(player.score_summary[constants.SCORE_LOSSES]):8}"
        + f"{str(player.score_summary[constants.SCORE_DRAWS]):8}"
    )


def show_matrix(matrix, player_list):
    print("Results matrix")
    show_opponents(player_list)
    show_player_results(matrix, player_list)


def show_opponents(player_list):
    opponents = f"{'':12}"
    for player in player_list:
        opponents += f"{player.name:12} "
    print(opponents)


def show_player_results(matrix, player_list):
    for player1 in player_list:
        result_line = f"{player1.name:12}"
        for player2 in player_list:
            values = matrix[player1.id][player2.id]
            scores = ",".join([str(i) for i in values])
            result_line += f"{scores:12} "
        print(result_line)


if __name__ == "__main__":
    main()
