'''
62. Unique Paths
https://leetcode.com/problems/unique-paths/
https://leetcode.com/problems/unique-paths/discuss/184248/8-lines-Java-DP-solution-0ms-beats-100-explained-with-graph

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3

Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28

Input: m = 3, n = 3
Output: 6
'''

 def uniquePaths(n: int, m: int) -> int:
    dp = [[1] * m for _ in range(n)]
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    # return dp[n-1][m-1]
    return dp[-1][-1]