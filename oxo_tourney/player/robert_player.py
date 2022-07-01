from oxo_tourney.player.player import Player


class RobertPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board, symbol=""):
        size = board.size
        board_state = f"{board}".splitlines()
        board_state = "".join(board_state)
        board_list = []
        for i in range(board.size):
            temp = []
            for j in range(board.size):
                temp.append("-")
            board_list.append(temp)

        print(board_list)

"""
    def minimax(board, depth, player):
        if player == max:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or game_over(state):
            score = evaluate(state)
            return [-1, -1, score]

        for cell in empty_cells(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = minimax(state, depth - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == max:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score

        return best
    """