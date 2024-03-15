'''
200. Number of Islands
Link: https://leetcode.com/problems/number-of-islands/submissions/

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ['1', '1', '1', '1', '0'],
  ['1', '1', '0', '1', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '0', '0', '0']
]
Output: 1

Input: grid = [
  ['1', '1', '0', '0', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '1', '0', '0'],
  ['0', '0', '0', '1', '1']
]
Output: 3
'''


class Solution:
    '''
    Time Complexity O(V + E) -> Vertices -> Cell, Edges -> Directions
    V = N * M, E = 4 * (N * M)
    FINAL - N * M
    '''

    def num_of_lands(self, grid) -> int:
        count = 0
        n, m = len(grid), len(grid[0])

        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count += 1

        return count

    @property
    def directions(self):
        return [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def is_valid_cell(self, grid, row, col):
        n, m = len(grid), len(grid[0])
        return (0 <= row < n) and (0 <= col < m)

    def dfs(self, grid, row, col):
        '''SINK ISLAND'''

        out_bounds = not self.is_valid_cell(grid, row, col)
        if out_bounds or grid[row][col] == '0':
            return

        grid[row][col] = '0'  # SINK

        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)

    def dfs_v2(self, grid, row, col):
        '''SINK ISLAND'''

        out_of_bounds = not self.is_valid_cell(grid, row, col)
        if out_of_bounds or grid[row][col] == '0':
            return

        grid[row][col] = '0'  # SINK

        for dx, dy in self.directions:
            self.dfs(grid, row + dx, col + dy)


soln = Solution()

grid1 = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
assert soln.num_of_lands(grid1) == 1

grid2 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
assert soln.num_of_lands(grid2) == 3
