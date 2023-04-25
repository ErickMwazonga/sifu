'''
1905. Count Sub Islands
Link: https://leetcode.com/problems/count-sub-islands/

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water)
and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical).
Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains 
all the cells that make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.
'''

Matrix = list[list[int]]


class Solution:
    '''
    IDEA:
    👉 firstly remove all the non-common island
    👉 Now count the sub-islands
    '''

    def countSubIslands(self, grid1: Matrix, grid2: Matrix) -> int:
        n, m = len(grid2), len(grid2[0])

        # removing all the non-common sub-islands
        for row in range(n):
            for col in range(m):
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    self.sink_island(grid2, row, col)

        remaining_sub_islands = self.count_islands(grid2)
        return remaining_sub_islands

    def is_cell_outside(self, grid, row, col):
        n, m = len(grid), len(grid[0])
        return row < 0 or row >= n or col < 0 or col >= m

    def count_islands(self, grid):
        n, m = len(grid), len(grid[0])
        _count = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    _count += 1
                    self.sink_island(grid, row, col)

        return _count

    def sink_island(self, grid, row, col):
        if self.is_cell_outside(grid, row, col):
            return

        if grid[row][col] == 0:
            return

        grid[row][col] = 0  # VISITED/SINK
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for x, y in directions:
            self.sink_island(grid, row + x, col + y)
