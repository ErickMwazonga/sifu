'''
1905. Count Sub Islands
https://leetcode.com/problems/count-sub-islands/

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water)
and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical).
Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains 
all the cells that make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.

'''


class Solution:
    '''
    IDEA:
    👉 firstly remove all the non-common island
    👉 Now count the sub-islands
    '''

    def countSubIslands(self, grid1, grid2) -> int:
        n, m = len(grid2), len(grid2[0])

        # removing all the non-common sub-islands
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    self.dfs(grid2, i, j)

        # counting sub-islands
        _count = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    self.dfs(grid2, i, j)
                    _count += 1
        return _count

    def dfs(self, grid, i, j):
        # n, m = len(grid), len(grid[i])
        outside = i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i])

        if outside or grid[i][j] == 0:
            return

        grid[i][j] = 0  # SINK
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i-1, j)
