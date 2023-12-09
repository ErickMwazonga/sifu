'''
419. Battleships in a Board
https://leetcode.com/problems/battleships-in-a-board/

Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board.
In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column),
where k can be of any size.
At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example:
[
    ['X', '.', '.', 'X'],
    ['.', '.', '.', 'X'],  --> 2
    ['.', '.', '.', 'X']
]
'''
class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        n, m = len(board), len(board[0])
        _count = 0

        for row in range(n):
            for col in range(m):
                if board[row][col] == 'X':
                    self.dfs(board, row, col)
                    _count += 1

        return _count

    def dfs(self, board, row, col):
        n, m = len(board), len(board[0])

        if not self.in_bounds(board, row, col):
            return

        if board[row][col] != 'X':
            return

        board[row][col] = '#' # sink

        self.dfs(board, row + 1,col)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row, col - 1)

    def dfs_v2(self, board, row, col):
        if not self.in_bounds(board, row, col):
            return

        if board[row][col] != 'X':
            return

        board[row][col] = '#'

        for dx, dy in self.directions:
            self.dfs(board, row + dx, col + dy)

    @property
    def directions(self):
        return [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def in_bounds(self, image, row, col):
        n, m = len(image), len(image[0])
        return (0 <= row < n) and (0 <= col < m)
