'''
https://leetcode.com/problems/search-a-2d-matrix-ii/
https://levelup.gitconnected.com/make-way-for-the-matrix-a-complete-guide-to-solving-2d-array-coding-problems-725096d122d9
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


class Solution:

    def searchMatrix(self, matrix, target):
        n_rows, n_cols = len(matrix), len(matrix[0])

        if not n_rows or not n_cols:
            return False

        maxRow, maxCol = n_rows - 1, n_cols - 1
        row, col = 0, maxCol

        while row <= maxRow and col >= 0:
            current_value = matrix[row][col]

            if current_value == target:
                return True
            elif current_value < target:
                row += 1
            else:
                col -= 1
        
        return False
