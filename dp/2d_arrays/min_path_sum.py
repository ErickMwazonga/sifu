'''
64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''


def min_path_sum(grid):
    if not grid:
        return

    n, m = len(grid), len[grid[0]]

    dp = [[0] * m for i in range(n)]
    dp[0][0] = grid[0][0]

    # first row
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # First column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # inner matrix
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

    return dp[n - 1][m - 1]


# OTHER SOLUTIONS
# ------------------------------------------------
# By using recursion:
def minimum_cost_path(matrix, i=0, j=0):
    ''' Time - O(2^nm), Space - O(nm) '''

    n = len(matrix)
    m = len(matrix[0])

    if i == n-1 and j == m-1:
        return matrix[i][j]
    elif i == n-1:
        return matrix[i][j] + minimum_cost_path(matrix, i, j+1)
    elif j == m-1:
        return matrix[i][j] + minimum_cost_path(matrix, i+1, j)
    else:
        return matrix[i][j] + min(
            minimum_cost_path(matrix, i+1, j),
            minimum_cost_path(matrix, i, j+1)
        )


def minimum_cost_path_v2(matrix):
    '''DP: Time - O(2^nm), Space - O(nm) '''

    n = len(matrix)
    m = len(matrix[0])

    costs = [[0] * m for i in range(n)]
    costs[0][0] = matrix[0][0]

    for i in range(1, m):
        costs[0][i] = costs[0][i-1] + matrix[0][i]

    for i in range(1, n):
        costs[i][0] = costs[i-1][0] + matrix[i][0]

    for i in range(1, n):
        for j in range(1, m):
            costs[i][j] = min(costs[i-1][j], costs[i][j-1]) + matrix[i][j]

    return costs[n-1][m-1]
