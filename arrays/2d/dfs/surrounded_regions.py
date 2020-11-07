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

        n_rows, n_cols = len(board), len(board[0])

        # change left and right border O into D
        for row in range(n_rows):
            self.dfs(board, row, 0)
            self.dfs(board, row, n_cols - 1)
        
        # change up and down border O into D
        for col in range(n_cols):
            self.dfs(board, 0, col)
            self.dfs(board, n_rows - 1, col)

        for row in range(n_rows):
            for col in range(n_cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'D':
                    board[row][col] = 'O'
    
    def helper(self, board, i: int, j: int) -> None:
        n_rows, n_cols = len(board), len(board[0])

        if i >= 0 and i < n_rows and j >= 0 and j < n_cols:
            if board[i][j] == 'O':
                board[i][j] = 'D'
                self.dfs(board, i + 1, j)
                self.dfs(board, i - 1, j)
                self.dfs(board, i, j + 1)
                self.dfs(board, i, j - 1)