'''
74. Search a 2D Matrix
Link: https://leetcode.com/problems/search-a-2d-matrix/
Credit: https://levelup.gitconnected.com/make-way-for-the-matrix-a-complete-guide-to-solving-2d-array-coding-problems-725096d122d9

Write an efficient algorithm that searches
for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row

Examples:
Input:
matrix = [[1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]]
target = 3
Output: true

Input:
matrix = [[1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]]
target = 13
Output: false
'''


def binary_search(row, target):
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


def searchMatrix(matrix, target):
    '''BRUTE FORCE SOLUTION -> O(NM)'''

    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True

    return False


def searchMatrix0(matrix, target):
    '''BINARY SEARCH ON EACH ROW -> O(nlog(m))'''

    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        if binary_search(matrix[i], target):
            return True

    return False


def searchMatrix1(matrix, target):
    '''CONVERT IT TO A SINGLE LIST THEN BINARY SEARCH - O(log(NM))'''

    flat_list = sum(matrix, [])
    return binary_search(flat_list, target)


def searchMatrix2(matrix, target: int) -> bool:
    '''BINARY SEARCH FOR THE ROWS THEN COLUMNS O(nlogn(nlogn))'''

    if not matrix:
        return False

    n_rows = len(matrix)
    low, high = 0, n_rows

    # outer binary search to select the row
    while low < high:
        mid_row_index = (low + high) // 2
        # inner binary search on the row
        found = binary_search(matrix[mid_row_index], target)

        if found:
            return True
        elif target > matrix[mid_row_index][-1]:
            low = mid_row_index + 1
        else:
            high = mid_row_index

    return False


def searchMatrix3(matrix, target: int) -> bool:
    '''Time: O(log(nm)) - https://www.youtube.com/watch?v=eT0UqrYuqbg'''

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


def searchMatrix5(matrix, target):
    '''ITERATE INTELLIGENTLY: Time: O(M*N)'''

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


def solutionx(matrix, target):
    # BINARY SEARCH ROWS - To get the row with target
    # BINARY SEARCH JUST on the found row

    # Resource: https://www.youtube.com/watch?v=Ber2pi2C0j0
    # Resource: https://github.com/neetcode-gh/leetcode/blob/main/74-Search-a-2D-Matrix.py

    ...