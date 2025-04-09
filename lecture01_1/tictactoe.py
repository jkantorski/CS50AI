"""
Tic Tac Toe Player
"""

import math
import copy

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
    xexits = 0
    oexits = 0
    if board == initial_state():
        return X
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xexits += 1
            elif board[i][j] == O:
                oexits += 1
    if xexits <= oexits:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    avaible = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                avaible.add((i,j))
    return avaible



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if action not in actions(new_board):
        raise ValueError("Invalid action")
    i,j = action
    val = player(new_board)
    new_board[i][j] = val
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_lines = [
        # Poziome
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Pionowe
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Skosy
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]

    for line in winning_lines:
        if line[0] == line[1] == line[2] and line[0] != EMPTY:
            return line[0]  # Zwracamy X lub O jeśli cała linia jest zajęta

    return None  # Brak zwycięzcy


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for line in board:
        if EMPTY in line and (winner(board) is None):
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        best_move = None
        v = -math.inf
        for action in actions(board):
            if max(v, min_value(result(board, action))) == max_value(board):
                best_move = action
                return best_move
    if player(board) == O:
        if player(board) == O:
            v = math.inf
            best_move = None
            for action in actions(board):
                if min(v, max_value(result(board, action))) == min_value(board):
                    best_move = action
                    return best_move
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v