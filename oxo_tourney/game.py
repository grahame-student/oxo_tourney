from oxo_tourney import constants
from oxo_tourney.board import Board


class Game:
    def __init__(self, player1, player2, board_size):
        self.__symbols = [constants.PLAYER_1, constants.PLAYER_2]
        self.__players = [player1, player2]
        self.__next_player = 1
        self.__board_size = board_size
        self.__board = None

    def start(self):
        self.__show_intro()
        self.__play_game()
        self.__show_outro()
        return self.__get_result()

    def __show_intro(self):
        print(f"New game {self.__players[0].name} Vs {self.__players[1].name}")

    def __play_game(self):
        self.__board = Board(self.__board_size)
        while self.__board.state is constants.STATE_IN_PROGRESS:
            self.__next_turn()

    def __next_turn(self):
        self.__get_next_player()
        self.__display_board()
        move = self.__get_move()
        self.__make_move(move)

    def __get_next_player(self):
        self.__next_player = (self.__next_player + 1) % 2

    def __display_board(self):
        print(self.__board)

    def __make_move(self, move):
        self.__board.set_cell(move[0], move[1], self.__symbols[self.__next_player])

    def __get_move(self):
        while True:
            move = self.__players[self.__next_player].get_move(
                self.__board, self.__symbols[self.__next_player]
            )
            if self.__board.valid_move(move[0], move[1]):
                break
            print("Invalid move, try again")
        return move

    def __show_outro(self):
        print()
        print("Game over")
        self.__display_board()

    def __get_result(self):
        return [self.__board.state, self.__board.winner]
