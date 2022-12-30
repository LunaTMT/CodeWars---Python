# https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/python
# Kata Author: suuuzi
# 5 kyu

import numpy as np

def done_or_not(board): 
    
    board = np.array(board)
    valid = {1,2,3,4,5,6,7,8,9}
    
    for i in range(9):
        
        #row + column check
        row = board[i,:]
        column = board[:,i]
        if set(row) != valid or set(column) != valid:
            return 'Try again!'

        #square check
        if i in [0, 3, 6]:
            for j in range(0, 9, 3):
                square = board[i:i+3, j:j+3].flatten()
                if set(square) != valid:
                    return 'Try again!'
  
    return 'Finished!'


if __name__ == "__main__":
    done_or_not([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [2, 3, 4, 5, 6, 7, 8, 9, 1],
                 [3, 4, 5, 6, 7, 8, 9, 1, 2],        
                 [4, 5, 6, 7, 8, 9, 1, 2, 3],
                 [5, 6, 7, 8, 9, 1, 2, 3, 4],
                 [6, 7, 8, 9, 1, 2, 3, 4, 5],            
                 [7, 8, 9, 1, 2, 3, 4, 5, 6],
                 [8, 9, 1, 2, 3, 4, 5, 6, 7],
                 [9, 1, 2, 3, 4, 5, 6, 7, 8]])
