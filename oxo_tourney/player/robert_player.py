from oxo_tourney.player.player import Player


class RobertPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.ROBERT = 1
        self.OTHER = -1

    def wins(self, board_list, player):
        size = len(board_list)
        # Check columns
        for col in range(size):
            result = 0
            for row in range(size):
                if board_list[col][row] == player:
                    result += 1
            if result == size:
                return True

        # Check rows
        for row in range(size):
            result = 0
            for col in range(size):
                if board_list[col][row] == player:
                    result += 1
            if result == size:
                return True

        # First Diagonal
        result = 0
        for cell in range(size):
            if board_list[cell][cell] == player:
                result += 1
        if result == size:
            return True

        # Second Diagonal
        result = 0
        last = size - 1
        for cell in range(size):
            if board_list[cell][last] == player:
                result += 1
            last -= 1
        if result == size:
            return True

        return False

    def empty_cells(self, board_list):
        cells = []

        for x, col in enumerate(board_list):
            for y, cell in enumerate(col):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def evaluate(self, board_list):
        # returns +1 if Robert's AI wins; -1 if the other AI wins; 0 draw
        if self.wins(board_list, self.ROBERT):
            score = +1
        elif self.wins(board_list, self.OTHER):
            score = -1
        else:
            score = 0

        return score

    def game_over(self, board_list):
        # Checks if either player has won the game
        return self.wins(board_list, self.ROBERT) or self.wins(board_list, self.OTHER)

    def minimax(self, board_list, depth, player):
        if depth == 0 or self.game_over(board_list):
            score = self.evaluate(board_list)
            return [-1, -1, score]

        if player == 1:
            best = [-1, -1, -10]
        else:
            best = [-1, -1, +10]

        for cell in self.empty_cells(board_list):
            x, y = cell[0], cell[1]
            board_list[x][y] = player
            score = self.minimax(board_list, depth - 1, -player)
            board_list[x][y] = 0
            score[0], score[1] = x, y

            if player == 1:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score

        return best

    def get_move(self, board, symbol=""):
        size = int(board.size)
        board_state = f"{board}".splitlines()
        board_state = "".join(board_state)
        board_list = []
        for i in range(board.size):
            temp = []
            for j in range(board.size):
                temp.append(0)
            board_list.append(temp)

        element = 0
        for i in board_state:
            col = element % size
            row = int(element / size)
            if i == "X":
                if symbol == "X":
                    board_list[col][row] = 1
                else:
                    board_list[col][row] = -1
            elif i == "O":
                if symbol == "O":
                    board_list[col][row] = 1
                else:
                    board_list[col][row] = -1
            else:
                board_list[col][row] = 0
            element += 1
        best = self.minimax(board_list, len(self.empty_cells(board_list)), 1)
        return [best[0], best[1]]
