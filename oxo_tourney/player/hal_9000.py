####################################
# Author: David A, utilising base player structure
# Description: AI noughts and crosses player using minimax method
# Last modified: 07/07/22
####################################

"""
Given that I'm out this Monday, I've left these notes for work done here:

Notes:
    * This is an AI player that uses the minimax method to work out every possible move in a game using a recursive
      decision tree algorithm, by positively impacting good moves (+1) and by negatively impacting bad moves that
      allow the opposition player to win

    ** NOTE 1: Only works for 3x3 matrix games unfortunately, there is a bug somewhere in my verify_winner function.
               Increasing grid size leads to AI getting stuck in infinite loop, didn't get a chance to investigate fully

    * Things I did get time for:
        * Splitting the functionality out into various functions, starting this from beginning helped with the code
          e.g "get_move" boils down to a couple of function calls
        * Getting a minimax function that works
        * Tried to limit calling the class instance variables passed to functions to improve performance (mem saving)
        * Accounted for a potential error when swapping the player call order in "example.py", depending on which player
          gets called first, either it will be assigned "X" or "O" so the algorithm scoring "verify_winner" is written
          to bypass this issue
    * Things I ran out of time for/future improvements:
        * Control over tree depth would be nice to prevent a recursive error, caution when increasing board size
        * Debugging > 3x3 matrix game size issue
        * The minimax function has a lot of duplicate code functionality that can be reduced
        * Some functions such as "best_move_available" and "minimax" need to be shorter
        * Type-hinting and staticmethod identifier would be good too
"""

from copy import deepcopy
from oxo_tourney.player.player import Player


class HAL9000(Player):  # Improved name
    def __init__(self, name):
        super().__init__(name)
        self.board = None
        self.x_is_maximising = True

    def get_move(self, board, symbol):
        self.board = board

        generated_grid = self.convert_board_to_grid(board)  # convert board to format algorithm can interpet

        col, row = self.best_available_move(generated_grid, symbol)

        return [col, row]  # return optimum col, row move from AI player

    def convert_board_to_grid(self, board_layout):
        board_list = board_layout.__str__().split()  # splits a string into a list, accounts for "\n"
        # print(board_list[0])
        # print(len(board_list))
        row_list = []
        the_grid = []
        for index in range(0, len(board_list)):  # provides board size index
            for element in board_list[index]:  # loop through a "row"
                # print("Element: {0}".format(element))
                row_list.append(element)

            # append to "the_grid"
            the_grid.append(deepcopy(row_list))  # deepcopy is made to prevent this being a mem ref to "row_list"
            row_list.clear()                     # because otherwise, clearing row_list would clear contents from grid
        return the_grid

    def best_available_move(self, grid, symbol):
        best_move_col = 0
        best_move_row = 0
        best_score = -100
        for row in range(0, self.board.size):  # loop through rows and col number
            for col in range(0, self.board.size):
                # first check, is a spot available?
                if self.valid_move(col, row, grid):
                    #  print("Position at col: {0}, row:{1} which is '{2}' is available".
                    #  format(col, row, self.the_grid[row][col]))
                    grid[row][col] = symbol
                    score = self.minimax(0, False, symbol, grid)  # False as AI player just made move on duplicate grid
                    grid[row][col] = "."
                    if score > best_score:  # remember rows and columns will be swapped
                        best_score = score  # update new score continuously
                        best_move_row = row
                        best_move_col = col

        print("AI has chosen position: col:{0}, row:{1}".format(best_move_col, best_move_row))
        return best_move_col, best_move_row

    def minimax(self, depth, is_maximising, symbol, grid):  # depth is not yet implemented!

        score = self.verify_winner(symbol, grid)
        if score is not None:  # terminal state (where the code has reached the bottom of a decision tree)
            return score

        if is_maximising:  # so other player just made a move on copied grid
            best_score = -100
            for row in range(0, self.board.size):  # loop through rows and col number
                for col in range(0, self.board.size):
                    if self.valid_move(col, row, grid):
                        grid[row][col] = symbol  # so now ai player makes a move on copied grid
                        score = self.minimax(0, False, symbol, grid)  # now we pass back to the other player
                        grid[row][col] = "."   # clear past moves - grid can be used for trying a different sequences
                        if score > best_score:
                            best_score = score  # update new score
            return best_score

        if not is_maximising:  # so AI player just made a move on copied grid
            best_score = 100
            for row in range(0, self.board.size):  # loop through rows and col number
                for col in range(0, self.board.size):
                    if self.valid_move(col, row, grid):  # so now other player makes a move on copied grid
                        if self.x_is_maximising:
                            grid[row][col] = "O"
                        else:
                            grid[row][col] = "X"
                        score = self.minimax(0, True, symbol, grid)  # now pass back to the AI player
                        grid[row][col] = "."
                        if score < best_score:
                            best_score = score  # update new score

            return best_score

    def verify_winner(self, symbol, grid):

        result = None
        # Identify maximising player, we need this due to player function order calling in "example.py" -> player_list[]
        if symbol == "X":
            self.x_is_maximising = True
        else:
            self.x_is_maximising = False

        if self.x_is_maximising:
            if self.board_match_state(symbol, grid) > 0:  # if x is maximising then return +1 score for cool moves
                result = 1
            elif self.board_match_state("O", grid) > 0:
                result = -1
        else:
            if self.board_match_state(symbol, grid) > 0:  # if y is maximising then return +1 score for cool moves
                result = 1
            elif self.board_match_state("X", grid) > 0:
                result = -1
        if self.is_full(grid):  # check draw scenario
            result = 0

        return result

    def board_match_state(self, symbol, grid):
        lines = self.check_horizontal(symbol, grid)
        lines += self.check_vertical(symbol, grid)
        lines += self.check_diagonal(symbol, grid)
        return lines

    def check_horizontal(self, symbol, grid):
        result = 0
        for row in range(0, self.board.size):
            if grid[row] == symbol * self.board.size:
                result += 1
        return result

    def check_vertical(self, symbol, grid):
        result = 0
        for col in range(0, self.board.size):
            line = True
            for row in range(0, self.board.size):
                line &= (grid[row][col]) == symbol
            if line:
                result += 1
        return result

    def check_diagonal(self, symbol, grid):
        result = 0
        max_col = self.board.size - 1
        line_dr = True  # \
        line_dl = True  # /
        for row in range(0, self.board.size):
            line_dr &= grid[row][row] == symbol
            line_dl &= grid[row][max_col - row] == symbol
        if line_dl | line_dr:
            result += 1
        return result

    def is_full(self, grid):
        count = 0
        for row in grid:
            count += row.count(".")
        return count == 0

    def valid_move(self, col, row, grid):
        return grid[row][col] == "."



