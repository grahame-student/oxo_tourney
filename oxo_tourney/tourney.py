from oxo_tourney import constants
from oxo_tourney.game import Game


class Tourney:
    def __init__(self, player_list):
        self.__players = player_list
        self.score_matrix = self.__get_matrix()

    def __get_matrix(self):
        result = {}
        for player1 in self.__players:
            result_list = {}
            for player2 in self.__players:
                result_list[player2.id] = [0, 0, 0]
            result[player1.id] = result_list
        return result

    def start(self, play_self=False):
        for player1 in self.__players:
            for player2 in self.__players:
                game_result = self.__play_game(play_self, player1, player2)
                self.__update_score_summary(game_result, player1, player2)

    def __play_game(self, play_self, player1, player2):
        game_result = [None, None]
        if not play_self and player1 != player2:
            game = Game(player1, player2, 3)
            game_result = game.start()
            self.__update_score_matrix(game_result, player1, player2)
        return game_result

    @staticmethod
    def __update_score_summary(game_result, player1, player2):
        if game_result[0] == constants.STATE_DRAW:
            Tourney.__update_draw_scores(player1, player2)
        elif game_result[0] == constants.STATE_WIN:
            Tourney.__update_win_loss_scores(game_result, player1, player2)

    @staticmethod
    def __update_draw_scores(player1, player2):
        player1.score_summary[constants.SCORE_DRAWS] += 1
        player2.score_summary[constants.SCORE_DRAWS] += 1

    @staticmethod
    def __update_win_loss_scores(game_result, player1, player2):
        if game_result[1] == constants.PLAYER_1:
            player1.score_summary[constants.SCORE_WINS] += 1
            player2.score_summary[constants.SCORE_LOSSES] += 1
        else:
            player1.score_summary[constants.SCORE_LOSSES] += 1
            player2.score_summary[constants.SCORE_WINS] += 1

    def __update_score_matrix(self, game_result, player1, player2):
        if game_result[0] == constants.STATE_DRAW:
            self.score_matrix[player1.id][player2.id][constants.SCORE_DRAWS] += 1
            self.score_matrix[player2.id][player1.id][constants.SCORE_DRAWS] += 1

        if game_result[0] == constants.STATE_WIN:
            if game_result[1] == constants.PLAYER_1:
                self.score_matrix[player1.id][player2.id][constants.SCORE_WINS] += 1
                self.score_matrix[player2.id][player1.id][constants.SCORE_LOSSES] += 1
            else:
                self.score_matrix[player1.id][player2.id][constants.SCORE_LOSSES] += 1
                self.score_matrix[player2.id][player1.id][constants.SCORE_WINS] += 1
