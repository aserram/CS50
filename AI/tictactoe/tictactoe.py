"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_player = 0
    o_player = 0
    for states in board:
        x_player += states.count(X)
        o_player += states.count(O)
    if x_player > o_player:
        return O
    if x_player <= o_player:
        return X


def actions(board):
    moves = set()
    for row_idx in range(len(board)):
        for col_idx in range(len(board[row_idx])):
            if board[row_idx][col_idx] == EMPTY:
                moves.add((row_idx, col_idx))
    return moves


def result(board, action):
    result_board = deepcopy(board)
    result_board[action[0][action[1]]] = player(board)
    return result_board


def winner(board):
    players = (X, O)
    for player in players:
        # Check rows
        for row in board:
            if all(cell == player for cell in row):
                return player

        # Check columns
        for col in range(3):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                return player

        # Check diagonals
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return player
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return player

    return None


def terminal(board):
    # Check for winner
    if winner(board) is not None:
        return True
    # Check if board is full
    elif all(all(row) for row in board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
