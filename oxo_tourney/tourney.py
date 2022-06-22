class Tourney:
    def __init__(self, player_list):
        self.__players = player_list

    def start(self):
        results = []
        for player1 in self.__players:
            for player2 in self.__players:
                if player1 == player2:
                    continue
                print(f"{player1.name} vs {player2.name}")
                results.append([])
        return results
