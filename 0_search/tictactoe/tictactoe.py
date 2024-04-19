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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    flat_board = flat(board)
    empty_spaces = flat_board.count(EMPTY)

    if empty_spaces % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    new_board = [row.copy() for row in board]
    new_board[action[0]][action[1]] = current_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    flat_board = flat(board)
    empty_spaces = flat_board.count(EMPTY)

    if empty_spaces == 9:
        return None
    else:
        # TODO - check if there is a winner
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    flat_board = flat(board)
    empty_spaces = flat_board.count(EMPTY)

    if empty_spaces == 9:
        return False
    else:
        # TODO - check if there is a winner
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # TODO - Implement this
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return (0,0)


# Helper functions

def flat(list):
    return sum(list, [])


def terminal_board():
    return [[X, O, X],
            [O, X, O],
            [X, O, X]]