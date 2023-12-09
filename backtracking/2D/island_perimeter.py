'''
463. Island Perimeter
Link: https://leetcode.com/problems/island-perimeter/description/
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4
'''


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    return self.dfs(grid, row, col)

        return -1

    @property
    def directions(self):
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def in_bounds(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return (0 <= x < n) and (0 <= y < m)

    def dfs(self, grid, row, col):
        if not self.in_bounds(grid, row, col):
            return 1

        if grid[row][col] == 0:
            return 1

        if grid[row][col] == '#':
            return 0

        grid[row][col] = '#'
        curr_count = 0
        for dx, dy in self.directions:
            x, y = row + dx, col + dy
            curr_count += self.dfs(grid, x, y)

        return curr_count
