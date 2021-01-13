'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/submissions/

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
            
        count = 0
        n, m = len(grid), len(grid[0])

        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count += 1
                    
        return count
    
    def dfs(self, grid, row, col):
        n, m = len(grid), len(grid[0])
        
        if row < 0 or col < 0 or row >= n or col >= m or grid[row][col] == '0':
            return 
        
        grid[row][col] = '0' # SINK
        
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)