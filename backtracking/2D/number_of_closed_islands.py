'''
1254. Number of Closed Islands
https://leetcode.com/problems/number-of-closed-islands/description/

Given a 2D grid consists of 0s (land) and 1s (water).
An island is a maximal 4-directionally connected group of 0s and
a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:
Input: grid = [
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]
]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0], [0,1,0,1,0], [0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,1,0,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]
]
Output: 2


INTUITION:
    IF WE ARE OUT OF THE BOUNDARIES -> ABSOLUTELY FALSE
'''

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0 and self.dfs(grid, row, col):
                    count += 1

        return count

    def dfs(self, grid, row, col):
        if not self.in_bounds(grid, row, col):
            return False

        if grid[row][col] == 1 or grid[row][col] == '#':
            return True

        grid[row][col] = '#'

        boundaries = []
        for dx, dy in self.directions:
            boundaries.append(
                self.dfs(grid, row + dx, col + dy)
            )

        return all(boundaries)

    def in_bounds(self, grid, row, col):
        n, m = len(grid), len(grid[0])
        return (0 <= row < n) and (0 <= col < m)

    @property
    def directions(self):
        return [(0, -1), (0, 1), (-1, 0), (1, 0)]
