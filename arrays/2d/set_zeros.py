'''
73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0,
set its entire row and column to 0. Do it in-place.

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
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
