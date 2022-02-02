'''
130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O'
on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''


class Solution:
    def solve(self, board) -> None:
        if not board:
            return

        n, m = len(board), len(board[0])

        # change left and right border O into D
        for row in range(n):
            self.dfs(board, row, 0)
            self.dfs(board, row, m - 1)

        # change up and down border O into D
        for col in range(m):
            self.dfs(board, 0, col)
            self.dfs(board, n - 1, col)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'

    def dfs(self, board, i: int, j: int) -> None:
        n, m = len(board), len(board[0])

        if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != 'O':
            return

        board[i][j] = 'D'  # SURROUND

        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)
