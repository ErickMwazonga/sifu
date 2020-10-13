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


def set_zeros(A):
    zeros = {'rows': set(), 'cols': set()}

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                zeros['rows'].add(i)
                zeros['cols'].add(j)

    for i in range(len(A)):
        for j in range(len(A[0])):
            if i in zeros['rows']:
                A[i] = [0] * len(A[0])
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
