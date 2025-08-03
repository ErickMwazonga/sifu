'''
2428. Maximum Sum of an Hourglass
https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

You are given an m x n integer matrix grid.
We define an hourglass as a part of the matrix with the following form:

Return the maximum sum of the elements of an hourglass.
Note that an hourglass cannot be rotated and must be entirely contained within the matrix.
'''

def maxSum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    max_sum = float('-inf')

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            hourglass = (
                grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] +
                grid[i][j] +
                grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
            )
            max_sum = max(max_sum, hourglass)

    return max_sum