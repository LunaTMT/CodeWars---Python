def numRookCaptures(board: list[list[str]]) -> int:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    rows = len(board)
    columns = len(board[0])

    start = [(r, c) for r, row in enumerate(board) for c, val in enumerate(row) if val == "R"][0]
    res = 0

    for (tx, ty) in zip(dx, dy):
        x, y = start
        found = False
        i = 1
        while (0 <= x < rows) and (0 <= y < columns) and board[x][y] not in ("p", "B"):
            if board[x][y] == "p":
                found = True
            x += (tx * i)
            y += (ty * i)
            i += 1
            
        if found:
            res += 1
    return res

numRookCaptures([[".",".",".",".",".",".",".","."],
                 [".",".",".","p",".",".",".","."],
                 [".","p",".","R",".",".",".","p"],
                 [".",".",".",".",".",".",".","."],
                 [".",".",".",".",".",".",".","."],
                 [".",".",".","p",".",".",".","."],
                 [".",".",".",".",".",".",".","."],
                 [".",".",".",".",".",".",".","."]])