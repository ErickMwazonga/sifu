'''
73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0,
set its entire row and column to 0. Do it in-place.

Input:
[
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
Output:
[
  [1, 0, 1],
  [0, 0, 0], 
  [1, 0, 1]
]
'''


def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """

    n, m = len(matrix), len(matrix[0])

    # Get the rows and cols that have 0 value
    rows, cols = set(), set()

    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    # traverse row wise and update columns
    for row in rows:
        for j in range(m):
            matrix[row][j] = 0

    # traverse column wise and update rows
    for col in cols:
        for row in range(n):
            matrix[row][col] = 0

    return matrix


def set_zeros(A):
    zeros = {'rows': set(), 'cols': set()}

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                zeros['rows'].add(i)
                zeros['cols'].add(j)

    for i in range(len(A)):
        for j in range(len(A[0])):
            if i in zeros['rows'] and A[i][j] != 0:
                A[i][j] = 0
            elif j in zeros['cols'] and A[i][j] != 0:
                A[i][j] = 0


'''
Time complexity for all three progression is O(m * n).
Space: O(1) for modification in place and using the first row
and first col to keep track of zeros instead of zeroes_row and zeroes_col
'''


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        m, n = len(matrix), len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0

        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                else:
                    matrix[row][col]

        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0


m = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

assert set_zeros(m) == [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1]
]
