'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
https://levelup.gitconnected.com/make-way-for-the-matrix-a-complete-guide-to-solving-2d-array-coding-problems-725096d122d9
Write an efficient algorithm that searches
for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''


def searchMatrix(matrix, target):
    '''Time: O(M*N)'''

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True

    return False


class Solution:
    '''
    Time: O(log(nm))
    https://www.youtube.com/watch?v=eT0UqrYuqbg
    '''

    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols

        while left < right:
            mid = left + (right - left) // 2
            i, j = mid // cols, mid % cols  # divmod(mid, cols)

            mid_elem = matrix[i][j]

            if mid_elem == target:
                return True
            elif mid_elem < target:
                left = mid + 1
            else:
                right = mid

        return False


def searchMatrix2(matrix, target) -> bool:
    '''Time: O(M*N)'''

    if not matrix:
        return False

    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        if target > matrix[i][-1]:
            i += 1
            continue

        if i >= n:
            return False

        for j in range(m):
            if target == matrix[i][j]:
                return True

    return False


def searchMatrix3(matrix, target):
    '''Time: O(M*N)'''

    if not matrix:
        return False

    n, m = len(matrix), len(matrix[0])
    i, j = 0, m - 1

    while i < n and j >= 0:
        if target == matrix[i][j]:
            return True
        elif target > matrix[i][j]:  # Move down a row
            i += 1
        else:  # Move left a column
            j -= 1

    return False


class SortedSearch:

    def binary_row_search(self, row, target):
        start, end = 0, len(row) - 1

        while start <= end:
            mid = (start + end) // 2

            if target == row[mid]:
                return True
            elif target > row[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return False

    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix:
            return False

        n_rows = len(matrix)
        start, end = 0, n_rows

        # outer binary search to select the row
        while start < end:
            mid_row = (start + end) // 2
            # inner binary search on the row
            found = self.binary_row_search(matrix[mid_row], target)
            if found:
                return True
            elif target > matrix[mid_row][-1]:
                start = mid_row + 1
            else:
                end = mid_row

        return False
