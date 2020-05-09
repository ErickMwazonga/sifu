'''
https://levelup.gitconnected.com/make-way-for-the-matrix-a-complete-guide-to-solving-2d-array-coding-problems-725096d122d9
'''

from typing import List
Matrix = List[List[int]]


def transpose(matrix: Matrix) -> Matrix:
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    res = [[0 for _ in range(n_rows)] for _ in range(n_cols)]

    for i in range(n_rows):
        for j in range(n_cols):
            res[j][i] = matrix[i][j]
    return res


input_x = [[1, 2], [3, 4], [5, 6]]
output_x = [[1, 3, 5], [2, 4, 6]]

assert transpose(input_x) == output_x
