'''
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array.
(If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11,
because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        if not grid:
            return 0

        max_count = 0
        n, m = len(grid), len(grid[0])

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    count = self.dfs(grid, row, col)
                    max_count = max(max_count, count)

        return max_count

    def dfs(self, grid, row, col):
        n, m = len(grid), len(grid[0])

        outside = row < 0 or col < 0 or row >= n or col >= m
        if outside or grid[row][col] == 0:
            return 0

        grid[row][col] = 0  # SINK

        right = self.dfs(grid, row, col + 1)
        left = self.dfs(grid, row, col - 1)
        down = self.dfs(grid, row + 1, col)
        up = self.dfs(grid, row - 1, col)

        return 1 + up + down + left + right


matrix = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]

soln = Solution()
assert soln.maxAreaOfIsland(matrix) == 6
