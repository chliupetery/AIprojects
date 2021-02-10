"""
Tic Tac Toe Player
"""

from math import inf
from copy import deepcopy 

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
    
    # iterate through the board and count numbers of X and O
    X_count = 0
    O_count = 0
    
    for row in board:
        X_count += row.count(X)
        O_count += row.count(O)
    return O if X_count > O_count else X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    PossibleAction = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                PossibleAction.add((i, j))

    return PossibleAction


  #  raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    CopyBoard = deepcopy(board)

    if CopyBoard[action[0]][action[1]] != EMPTY:
        raise Exception("Not an Empty Spot!")
    else:
        CopyBoard[action[0]][action[1]] = player(board)

    return CopyBoard

#    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
           return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
           return board[0][i]
    if ((board[0][0] == board[1][1] == board[2][2] != EMPTY) or (board[0][2] == board[1][1] == board[2][0] != EMPTY)):
        return board[1][1]
    return None
 #   raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

 #   raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
 #   raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    CurrentPlayer = player(board)

    if terminal(board):
        return None
    
    if CurrentPlayer == X:
        _ , OptimalAction = max_value(board)
    else:
        _ , OptimalAction = min_value(board)
    return OptimalAction

def max_value(board, alpha = -inf, beta = inf):
    if terminal(board):
        return utility(board), None
    BestValue, BestMove = -inf, None

    for action in actions(board):
        Value, _ = min_value(result(board, action), alpha, beta)
        if Value > BestValue:
            BestValue = Value
            BestMove = action
        alpha = max(alpha, BestValue)
        if alpha >= beta:
            break
    return BestValue, BestMove

def min_value(board, alpha = -inf, beta = inf):
    if terminal(board):
        return utility(board), None
    BestValue, BestMove = inf, None
    for action in actions(board):
        Value, _ = max_value(result(board, action), alpha, beta)
        if Value < BestValue:
            BestValue = Value
            BestMove = action
        beta = min(beta, BestValue)
        if alpha >= beta:
            break
    return BestValue, BestMove

 #   raise NotImplementedError
