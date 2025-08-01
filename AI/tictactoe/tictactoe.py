"""
Tic Tac Toe Player
"""

import math

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
    if x_player < o_player:
        return X
    else:
        return X


def actions(board):
    moves = []
    for row_idx in range(len(board)):
        for col_idx in range(len(board[row_idx])):
            if board[row_idx][col_idx] == EMPTY:
                moves.append((row_idx, col_idx))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


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
