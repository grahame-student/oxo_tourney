from oxo_tourney import constants


class Board:
    def __init__(self, board_size):
        self.state = constants.STATE_IN_PROGRESS
        self.winner = None
        self.size = board_size
        self.__grid = ["." * board_size] * board_size

    def __str__(self):
        result = ""
        for row in self.__grid:
            result += f"{row}\n"
        return result

    def valid_move(self, col, row):
        return self.__grid[row][col] == "."

    def set_cell(self, col, row, symbol):
        row_val = self.__grid[row]
        row_val = row_val[:col] + symbol + row_val[col + 1:]
        self.__grid[row] = row_val
        line_count = self.__check_lines(symbol)
        if line_count > 0:
            self.state = constants.STATE_WIN
            self.winner = symbol
        elif self.__is_full():
            self.state = constants.STATE_DRAW

    def __check_lines(self, symbol):
        lines = self.__check_horizontal(symbol)
        lines += self.__check_vertical(symbol)
        lines += self.__check_diagonal(symbol)
        return lines

    def __check_horizontal(self, symbol):
        result = 0
        for row in range(0, self.size):
            if self.__grid[row] == symbol * self.size:
                result += 1
        return result

    def __check_vertical(self, symbol):
        result = 0
        for col in range(0, self.size):
            line = True
            for row in range(0, self.size):
                line &= ((self.__grid[row][col]) == symbol)
            if line:
                result += 1
        return result

    def __check_diagonal(self, symbol):
        result = 0
        max_col = self.size - 1
        line_dr = True  # \
        line_dl = True  # /
        for row in range(0, self.size):
            line_dr &= (self.__grid[row][row] == symbol)
            line_dl &= (self.__grid[row][max_col - row] == symbol)
        if line_dl | line_dr:
            result += 1
        return result

    def __is_full(self):
        count = 0
        for row in self.__grid:
            count += row.count(".")
        return count == 0
