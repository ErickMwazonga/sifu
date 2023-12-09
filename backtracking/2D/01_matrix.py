'''
542. 01 Matrix
https://leetcode.com/problems/01-matrix/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

*FAILS ON LEETCODE*
'''


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        n, m = len(mat), len(mat[0])
        output = [[0 * m] for _ in range(n) ]

        for row in range(n):
            for col in range(m):
                if mat[row][col] != 0:
                    dist = self.dfs(mat, row, col, dist=0, visited=set())
                    output[row][col] = dist

        return output

    def dfs(self, mat, row, col, dist, visited):
        if not self.in_bounds(mat, row, col):
            return float('inf')

        cell = f'{row}{col}'
        if mat[row][col] == 0 or cell in visited:
            return dist

        visited.add(cell)

        min_distance = float('inf')
        for dx, dy in self.directions:
            curr_distance = self.dfs(mat, row + dx, col + dy, dist + 1, visited)
            min_distance = min(min_distance, curr_distance)

        return min_distance

    @property
    def directions(self):
        return [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def in_bounds(self, mat, row, col):
        n, m = len(mat), len(mat[0])
        return (0 <= row < n) and (0 <= col < m)
