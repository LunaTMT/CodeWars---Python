def determinant(matrix):
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
       
    else:
        result = 0
        for col in range(len(matrix[0])):
            minor = [[matrix[i][j] for j in range(len(matrix[i])) if j != col] for i in range(len(matrix)) if i != 0]
            result += (matrix[0][col] * determinant(minor)) * (-1 if col%2 else 1)
        return result
    
determinant([[2,4,2],[3,1,1],[1,2,0]])