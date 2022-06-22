class Tourney:
    def __init__(self, player_list):
        self.__players = player_list

    def start(self):
        results_summary = []                # player1.name, wins, losses, draws
        results_matrix = []                 # playerX vs playerY
        for player1 in self.__players:
            results_summary.append([player1.name, 0, 0, 0])
            results = []
            for player2 in self.__players:
                scores = [0, 0, 0]
                if player1 != player2:
                    # play game
                    pass
                results.append([scores[0], scores[1], scores[2]])  # wins, losses, draws
            results_matrix.append([player1.name, results])

        return results_summary, results_matrix
