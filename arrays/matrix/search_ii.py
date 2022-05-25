'''
240. Search a 2D Matrix II
Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
Credit: https://levelup.gitconnected.com/make-way-for-the-matrix-a-complete-guide-to-solving-2d-array-coding-problems-725096d122d9

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
'''


def search_matrix(matrix, target):
    if not matrix:
        return False

    n, m = len(matrix), len(matrix[0])
    i, j = 0, m - 1

    while i < n and j >= 0:
        current_value = matrix[i][j]

        if target == current_value:
            return True
        elif target > current_value:
            i += 1
        else:
            j -= 1

    return False
