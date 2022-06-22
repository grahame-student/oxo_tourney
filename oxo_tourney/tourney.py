class Tourney:
    def __init__(self, player_list):
        self.__players = player_list

    def start(self):
        results_summary = []
        results_matrix = []  # full factorial playerX vs playerY matrix
        for player1 in self.__players:
            # player1.name, wins, losses, draws
            results_summary.append([player1.name, 0, 0, 0])

            # player1.name, [[wins, losses, draws], [wins, losses, draws], ...]
            results = []

            for player2 in self.__players:
                # we could add an extra loop to play multiple times
                # wins, losses, draws
                scores = [0, 0, 0]
                # play game
                results.append([scores[0], scores[1], scores[2]])
            results_matrix.append([player1.name, results])

        return results_summary, results_matrix
