"""
Tic Tac Toe Player
"""

from copy import deepcopy
from math import inf


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY,EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
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
    for ii in range (3):
            for jj in range(3):
                if board[ii][jj]==EMPTY:
                    PossibleAction.add((ii,jj))
    return PossibleAction


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    Copyboard = deepcopy (board)

    if Copyboard[action[0]][action[1]] != EMPTY:
        raise Exception("Not an empty spot")
    else:
        Copyboard[action[0]][action[1]] = player(board)
    return Copyboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for ii in range(3):
        if board[ii][0]==board[ii][1]==board[ii][2]!=EMPTY:
            return board[ii][0]
        if board[0][ii]==board[1][ii]==board[2][ii]!=EMPTY:
            return board[0][ii]
    if (board[0][0]==board[1][1]==board[2][2]!=EMPTY) or (board[0][2]==board[1][1]==board[2][0]!=EMPTY):
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True #check any wins?
    for ii in range(3):
        for jj in range(3):
            if board[ii][jj] == EMPTY:
                return False  # check if still has empty spot
    return True # for draw





def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    CurrentPlayer = player(board)
    if terminal(board):
        return None
    
    if CurrentPlayer == X:
        _, BestAction = max_value(board)
    else:
        _, BestAction = min_value(board)
    return BestAction

def max_value(board, alpha = -inf, beta = inf):
    if terminal(board):
        return utility(board), None
    BestValue, BestMove = -inf, None

    for action in actions(board):
        Value, _ = min_value(result(board,action),alpha,beta)
        if Value > BestValue:
            BestValue=Value
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
        Value, _ = max_value(result(board,action),alpha,beta)
        if Value < BestValue:
            BestValue=Value
            BestMove = action
        beta = min(beta, BestValue)
        if alpha >= beta:
            break
    return BestValue, BestMove


