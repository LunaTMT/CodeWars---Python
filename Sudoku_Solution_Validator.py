#https://www.codewars.com/kata/529bf0e9bdf7657179000008
#4kyu


import numpy as np

valid_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

#Validate each row and column has only unique values from 1-9
def Unique_Vals(board):
    for i in range(0, len(board)): 
        if (set(board[i]) and set(board[:,i])) == valid_set:
            pass
        else:
            return False
    return True

#Validate each 3x3 Block has only unique values from 1-9
def Blocks(board):
    for i in range(0, len(board), 3):
        for j in range(0, len(board), 3):
            if set((board[i:i+3, j:j+3]).flatten()) == valid_set:
                pass
            else:
                return False
        return True
            

def valid_solution(board):  
    board = np.array(board)

    if Unique_Vals(board):
        if Blocks(board):
            return True
        else:
            return False
    return False
