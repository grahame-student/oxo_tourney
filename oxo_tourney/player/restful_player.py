import json

from oxo_tourney.player.player import Player

import requests


class RestfulPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board, symbol):
        if board.size != 3:
            print("Rest API only supports 3x3 boards")
            exit()

        base_url = "https://stujo-tic-tac-toe-stujo-v1.p.rapidapi.com"

        board_state = f"{board}".splitlines()
        board_state = "".join(board_state)
        board_state = board_state.replace(".", "-")

        url = f"{base_url}/{board_state}/{symbol}"

        headers = {
            "X-RapidAPI-Key": "06c1146f5fmshaa95fff403de62dp1da2efjsn0263107c10cf",
            "X-RapidAPI-Host": "stujo-tic-tac-toe-stujo-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        response = json.loads(response.text)

        row = int(response['recommendation'] / board.size)
        col = int(response['recommendation'] % board.size)

        print(f"{response['recommendation']} -> {col}, {row}")

        # Only ever chooses the same move, can't be used to play a complete game
        return [col, row]
