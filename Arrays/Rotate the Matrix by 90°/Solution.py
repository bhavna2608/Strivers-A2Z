from typing import *

def rotateMatrix(mat : List[List[int]]):
    # Write your code here.
    n = len(mat[0])
    for i in range(n):
        for j in range(i+1, n):
            # Swap elements across the diagonal
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for row in mat:
        row.reverse()

    pass
