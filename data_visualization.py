"""
CSC111 2021 Final Project - The L Game
This file is for visualizing the data and for getting AI to play against each other.

This file is Copyright (c) 2021 Siddarth Dagar, Daniel Zhu, and Bradley Mathi.
"""
import csv
import plotly.express as plt
from player import *
from typing import Any


def print_sample(games_file: str) -> None:
    """
    This is meant to be run on sample_game.csv to quickly look at it in string format.
    It is key to note that the sample_game is the black piece move, after red/blue pieces have moved
    """
    with open(games_file) as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            for i in range(len(row)):
                if i % 4 == 0 and i != 0:
                    print('\n')
                print(row[i])


def battle_royale(player1: Any, player2: Any) -> list:
    """
    This function has to AI's play against each other and plots the result of their games.
    """
    n = 100
    win_list = []
    player_access = {'red': player1, 'blue': player2}
    for i in range(n):
        new_game_board = Board()
        move_set = new_game_board.get_valid_moves()
        while len(move_set) != 0:
            # Finds the player for this turn
            curr_player = player_access[new_game_board.move_type]
            # Receives L-move coords from player
            l_move = curr_player.make_move(new_game_board)
            # Converts L-move coord to a new board
            new_game_board.board = l_move
            new_game_board.move_type = 'black'
            # determines possible neutral-move set and receives neutral-move from player
            move_set = new_game_board.get_valid_moves()
            neutral_move = curr_player.make_move(new_game_board)
            # changes board parameters to match move made by player and updates visual
            new_game_board.board = neutral_move
            new_game_board.is_red_move = not new_game_board.is_red_move
            if new_game_board.is_red_move:
                new_game_board.move_type = 'red'
            else:
                new_game_board.move_type = 'blue'
            # determines possible l-moves for next turn to check if the game can continue
            move_set = new_game_board.get_valid_moves()
        if new_game_board.is_red_move:
            win_list.append(0)
        else:
            win_list.append(1)
    return win_list


def plot_winrates(wins: list) -> None:
    """
    This function should use battle_royale results to plot results of the win rates.

    Assume wins is the list returned by battle_royale. A 1 corresponds to player1's win.
    """
    figure = plt.scatter(x=[x for x in range(1, len(wins) + 1)], y=wins)
    figure.update_layout(
        title="Win Percents",
        xaxis_title="Games Played",
        yaxis_title="Winner",
    )

    figure.show()


def plot_winpercent(wins: list) -> None:
    """
    This function should use battle_royale results to plot results of the win rates as percents of
    the total.

    Assume wins is the list returned by battle_royale. A 1 corresponds to player1's win.
    """
    figure = plt.scatter(x=[x for x in range(1, len(wins) + 1)],
                         y=cumulated(wins))
    figure.update_layout(
        title="Winrates",
        xaxis_title="Games Played",
        yaxis_title="Percentage of games won by Player 1",
    )

    figure.show()


def cumulated(lst: list) -> list:
    """
    This function should return the cumulative sum divided by 100 at each index of the list lst.

    Precondition:
        - lst != []
    """
    new_lst = []
    total = 0
    for item in lst:
        total += item
        new_lst.append(total/100)
    return new_lst
