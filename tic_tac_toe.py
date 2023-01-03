# https://www.codewars.com/kata/525caa5c1bf619d28c000335/python
# Kata Author: eugene-bulkin
# 5 kyu

import numpy as np

def win(line):
    if len(line) == 1:
        return next(iter(line))
    return False

def is_solved(board):
    board = np.array(board)
    diag_1 = set(np.fliplr(board).diagonal())
    diag_2 = set(np.diag(board))
    draw = True
    winner = [win(diag_1), win(diag_2)]

    for i in range(0, 3):
        row = board[i, :]
        column = board[:, i]

        if 0 in row:
            draw = False
        
        winner.append(win(set(row)))
        winner.append(win(set(column)))
    
    if not max(winner) and draw:
        return 0
    else:
        return max(winner) if max(winner) else -1
        



if __name__ == "__main__":

    # not yet finished
    board = [[0, 0, 1],
            [0, 1, 2],
            [2, 1, 0]]
    #is_solved(board)    #, -1)

    # winning row
    board = [[1, 1, 1],
            [0, 2, 2],
            [0, 0, 0]]
    #is_solved(board)    #, 1)

    # winning column
    board = [[2, 1, 2],
             [2, 1, 1],
             [1, 1, 2]]
    is_solved(board)    #, 1)

    # draw
    board = [[2, 1, 2],
            [2, 1, 1],
            [1, 2, 1]]
    is_solved(board)    #, 0)
