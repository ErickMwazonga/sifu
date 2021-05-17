'''
62. Unique Paths
https://leetcode.com/problems/unique-paths/
https://leetcode.com/problems/unique-paths/discuss/184248/8-lines-Java-DP-solution-0ms-beats-100-explained-with-graph

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
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


class Solution(object):

    # DP
    def uniquePaths(self, n: int, m: int) -> int:
        dp = [[1] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                right = dp[i][j-1]
                down = dp[i-1][j]
                dp[i][j] = right + down

        return dp[-1][-1]

    # RECURSION
    def gridTravelerRec(self, n, m) -> int:
        '''Time: O(2^n+m), Space: O(n+m)'''

        if m == 1 and n == 1:
            return 1

        if m == 0 or n == 0:
            return 0

        right = self.gridTravelerRec(n, m-1)
        down = self.gridTravelerRec(n-1, m)
        return right + down

    # MEMOIZATION
    def uniquePathsMemoized(self, m, n, memo={}):
        '''Time: O(n*m), Space: O(n+m)'''

        key = f'{m}-{n}'

        if key in memo:
            return memo[key]

        if m == 1 and n == 1:
            return 1

        if m == 0 or n == 0:
            return 0

        right = self.gridTravelerRec(n, m-1)
        down = self.gridTravelerRec(n-1, m)

        memo[key] = right + down
        return memo[key]
