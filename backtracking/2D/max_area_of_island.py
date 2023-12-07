'''
695. Max Area of Island
Link: https://leetcode.com/problems/max-area-of-island/

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array.
(If there is no island, the maximum area is 0.)

Example 1:
[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
Given the above grid, return 6. Note the answer is not 11,
because the island must be connected 4-directionally.
'''


class Solution:
    def max_area_of_island(self, grid) -> int:
        if not grid:
            return 0

        max_area = 0
        n, m = len(grid), len(grid[0])

        for row in range(n):
            for col in range(m):
                if grid[row][col] != 1:
                    continue
                curr_area = self.dfs(grid, row, col)
                max_area = max(max_area, curr_area)

        return max_area

    def get_directions(self):
        return [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def is_valid_cell(self, grid, row, col):
        n, m = len(grid), len(grid[0])
        return (0 <= row < n) and (0 <= col < m)

    def dfs(self, grid, row, col):
        out_bounds = self.is_valid_cell(grid, row, col)
        if out_bounds or grid[row][col] == 0:
            return 0

        area = 1
        grid[row][col] = 0  # SINK

        right = self.dfs(grid, row, col + 1)
        left = self.dfs(grid, row, col - 1)
        down = self.dfs(grid, row + 1, col)
        up = self.dfs(grid, row - 1, col)

        return area + up + down + left + right
		# return 1 + area + up + down + left + right

    def dfs_v2(self, grid, row, col):
        out_bounds = not self.is_valid_cell(grid, row, col)
        if out_bounds or grid[row][col] == 0:
            return 0


        grid[row][col] = 0  # SINK

        area = 1
        for x, y in self.get_directions():
            area += self.dfs(grid, row + x, col + y)

        return area


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
assert soln.max_area_of_island(matrix) == 6
