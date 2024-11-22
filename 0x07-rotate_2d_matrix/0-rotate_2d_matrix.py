#!/usr/bin/python3
"""Write a function that rotate an n x n - 2D matrix,
90 degrees clockwise.
Do not return anything. The matrix must be edited in-place.
Assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """Define the function that rotate a 2D
    matrix 90 degree clockwise
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    if (len(matrix) == len(matrix[0])):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
    return matrix
