'''
419. Battleships in a Board
https://leetcode.com/problems/battleships-in-a-board/

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', 
return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. 
In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. 
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
        output = 0
        
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'X':
                    self.dfs(board, row, col)
                    output += 1

        return output
    
    def dfs(self, board, row, col):
        n, m = len(board), len(board[0])
        
        out_bounds = (row < 0 or row >= n) or (col < 0 or col >= m)
        if out_bounds or board[row][col] != 'X':
            return
        
        board[row][col] = '#' # sink
        
        self.dfs(board, row + 1,col)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row, col - 1)