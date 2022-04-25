'''
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/submissions/

Given a m x n matrix, if an element is 0,
set its entire row and column to 0. Do it in-place.

Input:                               Output:
[                                    [
  [1, 1, 1],                           [1, 0, 1],
  [1, 0, 1],        ------>            [0, 0, 0],
  [1, 1, 1]                            [1, 0, 1]
]                                    ]
NB: Do not return anything, modify matrix in-place instead
'''


def set_zeroes(matrix) -> None:
    n, m = len(matrix), len(matrix[0])
    affected_rows, affected_cols = set(), set()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                affected_rows.add(i)
                affected_cols.add(j)

    for i in affected_rows:
        for j in range(m):
            matrix[i][j] = 0

    for i in affected_cols:
        for j in range(n):
            matrix[j][i] = 0


def set_zeroes_v2(A):
    n, m = len(A), len(A[0])
    affected_rows, affected_cols = set(), set()

    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                affected_rows.add(i)
                affected_cols.add(j)

    for i in range(n):
        for j in range(m):
            not_zero = A[i][j] != 0
            affected = (i in affected_rows) or (j in affected_cols)

            if not_zero and affected:
                A[i][j] = 0


_input = [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]]

output = [[1, 0, 1],
          [0, 0, 0],
          [1, 0, 1]]

assert set_zeroes(_input) == output
