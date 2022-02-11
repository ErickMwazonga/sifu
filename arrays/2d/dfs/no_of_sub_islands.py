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
    def count_sub_islands(self, grid1, grid2) -> int:
        num_sub_islands = 0

        for row in range(len(grid2)):
            for col in range(len(grid2[row])):
                # If grid2 is land, and grid2 is a sub-island of grid 1
                if grid2[row][col] == 1 and self.check_islands(grid1, grid2, row, col):
                    num_sub_islands += 1

        return num_sub_islands

    def check_islands(self, grid1, grid2, row, col):
        n, m = len(grid2), len(grid2[0])
        outside = row < 0 or row >= n or col < 0 or col >= m

        if outside or grid2[row][col] == 0:
            return True

        # If one of the cells in either grid is land and the other is water, then current cell can not be a sub-island.
        if (grid1[row][col] == 0 and grid2[row][col] == 1) or (grid1[row][col] == 1 and grid2[row][col] == 0):
            return False

        # grid1[row][col] == 1 and grid2[row][col] == 1:
        grid2[row][col] = 0

        left = self.check_islands(grid1, grid2, row, col - 1)
        right = self.check_islands(grid1, grid2, row, col + 1)
        top = self.check_islands(grid1, grid2, row - 1, col)
        bottom = self.check_islands(grid1, grid2, row + 1, col)

        return left and right and top and bottom
