'''
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
'''

# DP
'''
Time complexity: O(n*m)
Space complexity: O(n*m)
'''

def paths(matrix):
    n, m = len(matrix), len(matrix[0])

    dp = [([0] * m) for i in range(n)]
    dp[0][0] = 0 if (matrix[0][0] == 1) else 1
    
    for i in range(1, m):
        if matrix[0][i] == 1:
            dp[0][i] = 0
        else:
            dp[0][i] = dp[0][i-1]

    for i in range(1, n):
        if matrix[i][0] == 1:
            dp[i][0] = 0
        else:
            dp[i][0] = dp[i-1][0]

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]

# RECURSION
def paths(matrix, i = 0, j = 0):
    '''
    Time complexity: O(2^(n*m))
    Space complexity: O(n + m)
    '''
    n, m = len(matrix), len(matrix[0])

    if i > n-1 or j > m-1 or matrix[i][j] == 1:
        return 0
    elif i == n-1 and j == m-1:
        return 1
    else:
        return paths(matrix, i+1, j) + paths(matrix, i, j+1)