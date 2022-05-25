'''
59. Spiral Matrix II
Link: https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
'''


def generateMatrix(n: int):
    matrix = []

    if not n:
        return matrix

    matrix = [[None for _ in range(n)] for _ in range(n)]

    num = 1
    top, down = 0, n - 1
    left, right = 0, n - 1

    while left <= right and top <= down:
        # top row
        for i in range(left, right+1):
            matrix[top][i] = num
            num += 1
        top += 1

        # right col
        for i in range(top, down+1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # bottom row
        for i in range(right, left-1, -1):
            matrix[down][i] = num
            num += 1
        down -= 1

        # left col
        for i in range(down, top-1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix
