'''
LeetCode 64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''


class Solution:
    def minPathSum(self, grid):
        if not grid:
            return

        n, m = len(grid), len[grid[0]]

        dp = [[0 for i in range(0, m)] for i in range(0, n)] # min paths
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