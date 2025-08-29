'''
1219. Path with Maximum Gold
https://leetcode.com/problems/path-with-maximum-gold/description/

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:
Input: grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
Output: 24
Explanation:
[[0, 6, 0], 
 [5, 8, 7], 
 [0, 9, 0]]
Path to get the maximum gold,  9 -> 8 -> 7.

Example 2:
Input: grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
Output: 28
Explanation:
[[1, 0, 7], 
 [2, 0, 6], 
 [3, 4, 5], 
 [0, 3, 0], 
 [9, 0, 20]]
Path to get the maximum gold,  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
'''

from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.grid = grid
        n, m = len(self.grid), len(self.grid[0])
        max_gold = 0

        for row in range(n):
            for col in range(m):
                if self.grid[row][col] > 0:
                    max_gold = max(max_gold, self.dfs(row, col, 0))
        
        return max_gold

    def in_bounds(self, row, col):
        n, m = len(self.grid), len(self.grid[0])
        return 0 <= row < n and 0 <= col < m

    def dfs(self, row, col, total):
        if not self.in_bounds(row, col) or self.grid[row][col] == 0:
            return total

        gold = self.grid[row][col]
        total += gold
        self.grid[row][col] = 0  # mark visited

        max_path = total
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            max_path = max(max_path, self.dfs(row+dx, col+dy, total))

        self.grid[row][col] = gold  # backtrack

        return max_path

class SolutionV2:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_gold = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col]:
                    curr_chase = self.dfs(grid, row, col)
                    max_gold = max(max_gold, curr_chase)
        
        return max_gold

    def in_bounds(self, grid, row, col):
        n, m = len(grid), len(grid[0])
        return (0 <= row < n) and (0 <= col < m)

    def dfs(self, grid, row, col):
        if not self.in_bounds(grid, row, col) or not grid[row][col]:
            return 0
        
        gold = grid[row][col]
        grid[row][col] = 0 # mark visited

        max_path = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            max_path = max(max_path, self.dfs(grid, row + dx, col + dy))

        grid[row][col] = gold  # backtrack
        return gold + max_path
