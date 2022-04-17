'''
54. Spiral Matrix
Link: https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Examples 
[
    [1, 2, 3], 
    [4, 5, 6],      ----->  [1, 2, 3, 6, 9, 8, 7, 4, 5]          
    [7, 8, 9]
]

[
    [1,  2,  3,  4], 
    [5,  6,  7,  8],  ------>  [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]       
    [9, 10, 11, 12]
]
Output -
'''


def spiral_order(matrix):
    res = []

    if not matrix:
        return res

    while matrix:
        first_row = matrix.pop(0)
        res += first_row
        # res.extend(first_row)

        # last column
        for row in matrix:
            if row:
                res.append(row.pop())

        # last row
        if matrix:
            last_row_reversed = matrix.pop()[::-1]
            res += last_row_reversed
            # res.extend(reversed(matrix[-1]))

        # first column
        for row in matrix[::-1]:
            # for row in reversed(matrix):
            if row:
                res.append(row.pop(0))

    return res


def spiral_order2(matrix):
    res = []

    if not matrix:
        return res

    top, down = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while (top <= down and left <= right):
        # first row
        res.extend(matrix[top][left:right+1])
        top += 1

        # last column
        for i in range(top, down+1):
            res.append(matrix[i][right])
        right -= 1

        # last row
        if (top <= down):
            last_row = matrix[down][left:right+1]
            res.extend(last_row[::-1])
            down -= 1

        # first column
        if (left <= right):
            for i in range(down, top-1, -1):
                res.append(matrix[i][left])
            left += 1

    return res


def spiralOrder3(matrix, res=[]):
    if not matrix:
        return res

    # first row
    res += matrix.pop(0)

    # last column
    for row in matrix:
        if row:
            res.append(row.pop())

    # last row
    if matrix:
        res += matrix.pop()[::-1]

    # first column
    for row in matrix[::-1]:
        if row:
            res.append(row.pop(0))

    return spiralOrder3(matrix)


b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = [
    [1,  2,  3,   4],
    [5,  6,  7,   8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
assert spiral_order([[1]]) == [1]
assert spiral_order([[7], [9], [6]]) == [[7], [9], [6]]
assert spiral_order(b) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_order(c) == [
    1, 2, 3, 4, 8, 12, 16,
    15, 14, 13, 9, 5, 6, 7, 11, 10
]
