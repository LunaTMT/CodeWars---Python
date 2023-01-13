import numpy as np


puzzle = np.array([     [5,3,0,0,7,0,0,0,0],
                        [6,0,0,1,9,5,0,0,0],
                        [0,9,8,0,0,0,0,6,0],

                        [8,0,0,0,6,0,0,0,3],
                        [4,0,0,8,0,3,0,0,1],
                        [7,0,0,0,2,0,0,0,6],

                        [0,6,0,0,0,0,2,8,0],
                        [0,0,0,4,1,9,0,0,5],
                        [0,0,0,0,8,0,0,7,9]])


def solve(board):
    found = find_empty(board)
    if not found:
        return True #Board complete
    else:
        row, col = found



    for num in range(1,10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

def valid(board, num, pos):
    #num - number we're checking is correct
    #pos is current pos we're in for that given number (num)
    row, col = pos


    # Check row
    for i, value in enumerate(board[row, :]):
        if value == num and col != i: 
            return False

    # Check column
    for i, value in enumerate(board[:, col]):
        if value == num and row != i: 
            return False

    # Find what box current position is in
    x = col // 3
    y = row // 3
    box = board[y*3: (y*3 + 3), x*3 : (x*3 + 3)]

    for (i, j), value in np.ndenumerate(box):
        if value == num and (i,j) != pos:
            return False
    
    return True

def print_board(board):
    print("- - - - - - - - - - - - -")
    for i, row in enumerate(board):
        print("|", end = " ")
        
        for j in range(0, len(row), 3):    
            str_slice = ' '.join(map(str, board[i][j:j+3]))
            print(str_slice + " |", end = " ")

            if j == 6:
                print("")

        if i in [2, 5, 8] and i != 0:
            print("- - - - - - - - - - - - -")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)

    

if __name__ == "__main__":
    print_board(puzzle)
    solve(puzzle)
    print_board(puzzle)




