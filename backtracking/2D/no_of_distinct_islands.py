'''
694. Number of Distinct Islands (identical)
Link: https://leetcode.com/problems/number-of-distinct-islands/

Given a non-empty 2D arraygridof 0's and 1's, an island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only
if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
'''


class Solution:
    '''
    X - Start
    O - Out of bound OR Water
    U - Up
    D - Down
    R - Right
    L - Left
    '''

    def num_distinct_islands(self, grid):
        n, m = len(grid), len(grid[0])
        distinct_paths = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    path = self.compute_path(grid, i, j, 'X')
                    distinct_paths.add(path)

        return len(distinct_paths)

    @property
    def directions(self):
        return [(-1, 0, 'U'), (1, 0, 'D'), (0, 1, 'R'), (0, -1, 'L')]

    def is_valid_cell(self, grid, row, col):
        n, m = len(grid), len(grid[0])
        return (0 <= row < n) and (0 <= col < m)


    def compute_path(self, grid, i, j, direction):
        n, m = len(grid), len(grid[0])

        out_bounds = not self.is_valid_cell(grid, i, j)
        if out_bounds or grid[i][j] == 0:
            return 'O'

        grid[i][j] = 0  # SINK

        left = self.compute_path(grid, i, j - 1, 'L')
        right = self.compute_path(grid, i, j + 1, 'R')
        up = self.compute_path(grid, i - 1, j, 'U')
        down = self.compute_path(grid, i + 1, j, 'D')

        return direction + left + right + up + down

    def compute_path_v2(self, grid, i, j, direction):
        n, m = len(grid), len(grid[0])

        out_bounds = not self.is_valid_cell(grid, i, j)
        if out_bounds or grid[i][j] == 0:
            return 'O'

        grid[i][j] = 0  # SINK

        path = ''
        for dx, dy, dir_char in self.directions:
            path += self.compute_path(grid, i + dx, j + dy, dir_char)

        return direction + path


input1 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

input2 = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
]

soln = Solution()
assert soln.num_distinct_islands(input1) == 1
assert soln.num_distinct_islands(input2) == 3
