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
    # If the board is full we can't make a move
    flat_board = flat(board)
    empty_spaces = flat_board.count(EMPTY)
    if empty_spaces == 0:
        raise Exception("Game is over")
    
    # If the action is not valid we can't make a move
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid move")

    # Make the move
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
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2]:
                return row[0]
        # Check columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
                return board[0][i]
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
        
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return (i, j)
    return None


# Helper functions

def flat(list):
    return sum(list, [])
