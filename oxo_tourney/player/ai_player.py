from oxo_tourney.player.player import Player


class AiPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)
        self.__ai_symbol = None
        self.__opponent_symbol = None
        self.__board_state = None
        self.__board_size = None

    def get_move(self, board, ai_symbol: str):
        board_state = f"{board}".splitlines()
        self.__board_state = board_state
        self.__board_size = board.size
        self.__ai_symbol = ai_symbol
        self.__opponent_symbol = "O" if ai_symbol == "X" else "X"

        best_score = -100
        best_move = None

        for row in range(0, self.__board_size):
            for col in range(0, self.__board_size):
                if self.__board_state[row][col] == '.':
                    self.__board_state[row] = self.__get_row_val(ai_symbol, row, col)
                    score = self.__minimax(board_state, False)
                    self.__board_state[row] = self.__get_row_val('.', row, col)
                    if score > best_score:
                        best_score = score
                        best_move = [col, row]
        return best_move

    # returns optimal move using minimax algorithm
    def __minimax(self, board_state,  is_maximizing):
        if self.__is_ai_player_wins():
            return 1
        if self.__is_opponent_player_wins():
            return -1
        if self.__is_draw():
            return 0

        if is_maximizing:
            best_score = -1000
            for row in range(0, self.__board_size):
                for col in range(0, self.__board_size):
                    if board_state[row][col] == '.':
                        board_state[row] = self.__get_row_val(self.__ai_symbol, row, col)
                        score = self.__minimax(board_state, False)
                        board_state[row] = self.__get_row_val('.', row, col)
                        if score > best_score:
                            best_score = score
            return best_score
        else:
            best_score = 1000
            for row in range(0, self.__board_size):
                for col in range(0, self.__board_size):
                    if board_state[row][col] == '.':
                        board_state[row] = self.__get_row_val(self.__opponent_symbol, row, col)
                        score = self.__minimax(board_state, True)
                        board_state[row] = self.__get_row_val('.', row, col)
                        if score < best_score:
                            best_score = score
            return best_score

    def __get_row_val(self, symbol, row, col):
        row_val = self.__board_state[row]
        row_val = row_val[:col] + symbol + row_val[col + 1:]
        return row_val

    def __is_ai_player_wins(self):
        line_count = self.__check_lines(self.__ai_symbol)
        if line_count > 0:
            return True
        else:
            return False

    def __is_opponent_player_wins(self):
        line_count = self.__check_lines(self.__opponent_symbol)
        if line_count > 0:
            return True
        else:
            return False

    def __is_draw(self):
        count = 0
        for row in self.__board_state:
            count += row.count(".")
        return count == 0

    def __check_lines(self, symbol):
        lines = self.__check_horizontal(symbol)
        lines += self.__check_vertical(symbol)
        lines += self.__check_diagonal(symbol)
        return lines

    def __check_horizontal(self, symbol):
        result = 0
        for row in range(0, self.__board_size):
            if self.__board_state[row] == symbol * self.__board_size:
                result += 1
        return result

    def __check_vertical(self, symbol):
        result = 0
        for col in range(0, self.__board_size):
            line = True
            for row in range(0, self.__board_size):
                line &= (self.__board_state[row][col]) == symbol
            if line:
                result += 1
        return result

    def __check_diagonal(self, symbol):
        result = 0
        max_col = self.__board_size - 1
        line_dr = True  # \
        line_dl = True  # /
        for row in range(0, self.__board_size):
            line_dr &= self.__board_state[row][row] == symbol
            line_dl &= self.__board_state[row][max_col - row] == symbol
        if line_dl | line_dr:
            result += 1
        return result
