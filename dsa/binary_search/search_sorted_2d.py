'''
74. Search a 2D Matrix
Link: https://leetcode.com/problems/search-a-2d-matrix/
Resource: https://levelup.gitconnected.com/make-way-for-the-matrix-a-complete-guide-to-solving-2d-array-coding-problems-725096d122d9

Write an efficient algorithm that searches
for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row
Examples:
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

MATRIX = list[list[int]]


class Solution:
    '''
    Explanation: https://youtu.be/x-dYOtIudzc?list=PLKYEe2WisBTH7I9sCPjSZCs-iBAH4ybmS
    INTUITION: divmod(total_no_of_cells, no_of_cols) == row, col
    '''

    def searchMatrix(self, matrix, target: int):
        n, m = len(matrix), len(matrix[0])
        total_cells = n * m
        low, high = 0, total_cells - 1

        while low <= high:
            mid = (low + high) // 2
            row, col = divmod(mid, m)

            mid_val = matrix[row][col]
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1

        return False


class Solution_V1:

    def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        '''Time - N * M -> flattening the matrix'''

        nums = sum(matrix, []) # flatten matrix
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid - 1 
            else:
                low = mid + 1 

        return False

class Solution_V2:
    '''Time - log(M) + log(N)'''

    def searchMatrix(self, matrix: MATRIX, target: int):
        row = self.get_row(matrix, target)

        if row == -1:
            return False

        return binary_search(matrix[row], target)

    def get_row(self, matrix: MATRIX, target: int) -> list[int]:
        if not matrix:
            return False

        low, high = 0, len(matrix) - 1

        row = -1
        while low <= high:
            mid_row_index = (low + high) // 2

            if matrix[mid_row_index][0] <= target <= matrix[mid_row_index][-1]:
                return mid_row_index
            elif target > matrix[mid_row_index][-1]:
                low = mid_row_index + 1
            else:
                high = mid_row_index - 1

        return row


class Solution_V3:

    def search_matrix(self, matrix: MATRIX, target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])

        if not n_rows or not n_cols:
            return False

        start, end = 0, n_rows
        # outer binary search to select the row
        while start < end:
            mid_row = (start + end) // 2
            # inner binary search on the row
            found = binary_search(matrix[mid_row], target)
            if found:
                return True
            elif matrix[mid_row][-1] > target:
                end = mid_row - 1
            else:
                start = mid_row + 1

        return False


def binary_search(row: list[int], target: int) -> bool:
    '''HELPER FUNCTION: BINARY SEARCH'''

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
