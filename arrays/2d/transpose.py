'''
https://levelup.gitconnected.com/make-way-for-the-matrix-a-complete-guide-to-solving-2d-array-coding-problems-725096d122d9
'''

from typing import List
Matrix = List[List[int]]


def transpose(matrix: Matrix) -> Matrix:
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    transposed = [[0 for _ in range(n_rows)] for _ in range(n_cols)]

    for i in range(n_rows):
        for j in range(n_cols):
            transposed[j][i] = matrix[i][j]
    return transposed


input_x = [[1, 2], [3, 4], [5, 6]]
output_x = [[1, 3, 5], [2, 4, 6]]

assert transpose(input_x) == output_x


def transpose_square_in_place(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
print(transpose_square_in_place(m))
