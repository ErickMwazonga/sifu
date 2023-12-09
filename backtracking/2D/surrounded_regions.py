'''
130. Surrounded Regions
Link: https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input:                     Output
X X X X                    X X X X
X O O X     -------->      X X X X
X X O X                    X X X X
X O X X                    X O X X

Explanation:
Surrounded regions shouldn't be on the border, which means that any 'O'
on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

Matrix = list[list[str]]


class Solution:

    def solve(self, board: Matrix) -> None:
        if not board:
            return

        n, m = len(board), len(board[0])

        # surround left and right boarder with its environs
        for row in range(n):
            self.dfs(board, row, 0)
            self.dfs(board, row, m - 1)

        # surround top and bottom border with it's environs
        for col in range(m):
            self.dfs(board, 0, col)
            self.dfs(board, n - 1, col)

        for i in range(n):
            for j in range(m):
                val = board[i][j]

                if val == 'O':
                    board[i][j] = 'X'

                if val == '#':
                    board[i][j] = 'O'

    def dfs(self, board, i: int, j: int) -> None:
        n, m = len(board), len(board[0])

        out_bounds = i < 0 or i >= n or j < 0 or j >= m
        if out_bounds or board[i][j] != 'O':
            return

        board[i][j] = '#'  # SURROUND

        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)


class Solution2:

    def solve(self, grid: Matrix) -> None:
        n, m = len(grid), len(grid[0])

        # mark unsorrounded regions
        for row in range(n):
            for col in range(m):
                if self.is_open_boundary(grid, row, col):
                    self.sink_island(grid, row, col)

        # sink sorrounded regions
        for row in range(n):
            for col in range(m):
                # sink sorrounded regions
                if grid[row][col] == 'O':
                    grid[row][col] = 'X'

                # unmark unsorrounded regions
                if grid[row][col] == 'Q':
                    grid[row][col] = 'O'

    def is_open_boundary(self, grid, row, col):
        n, m = len(grid), len(grid[0])
        at_the_edge = (row == 0 or row == n - 1 or col == 0 or col == m - 1)
        return grid[row][col] == 'O' and at_the_edge

    def is_cell_outside(self, grid, row, col):
        n, m = len(grid), len(grid[0])
        return row < 0 or row >= n or col < 0 or col >= m

    def sink_island(self, grid, row, col):
        if self.is_cell_outside(grid, row, col):
            return

        if grid[row][col] != 'O':
            return

        grid[row][col] = 'Q'
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            self.sink_island(grid, row + dx, col + dy)
