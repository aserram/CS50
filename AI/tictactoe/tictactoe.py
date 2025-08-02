"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None
MINIMAX_ACT = (0, 0)


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

    if result_board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move action")
    if action[0] not in [0, 1, 2] or action[1] not in [0, 1, 2]:
        raise Exception("Invalid move action out of bounds")

    result_board[action[0]][action[1]] = player(board)
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
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board, idx):
    if terminal(board):
        return utility(board)

    max_v = -5
    for action in actions(board):
        v = min_value(result(board, action), idx + 1)
        if idx == 0 and v > max_v:
            global MINIMAX_ACT
            MINIMAX_ACT = action
        max_v = max(v, max_v)
    return max_v


def min_value(board, idx):
    if terminal(board):
        return utility(board)

    min_v = 5
    for action in actions(board):
        v = max_value(result(board, action), idx + 1)
        if idx == 0 and v < min_v:
            global MINIMAX_ACT
            MINIMAX_ACT = action
        min_v = min(v, min_v)
    return min_v


def minimax(board):
    if terminal(board):
        return None

    if player(board) == X:
        max_value(board, 0)
    else:
        min_value(board, 0)
    return MINIMAX_ACT
