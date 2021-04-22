#! /usr/bin/python3

# This program is a Game of Tic Tac Toe.
# It was produced during PCAP Certification

from random import choice


class game_board():
    def __init__(self):
        self.board = []
        print(self.board)


class player_setup():
    def __init__(self, name="Computer"):
        self.player = name
        self.games = 0
        self.games_won = 0


class game(player_setup):
    def __init__(self):
        player_setup()


try:
    numofplayers = int(input("How Many Players?: "))
    if numofplayers in [1, 2]:
        for i in range(numofplayers):
            pass
            # players[i] = player(input("Player1 Name: "))
    else:
        raise ValueError
except ValueError:
    print("Wrong Value: Please Input 1 or 2")
