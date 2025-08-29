'''
542. 01 Matrix
https://leetcode.com/problems/01-matrix/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
Output: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

Example 2:
Input: mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
Output: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
'''

from collections import deque

class Solution:
    '''
    BREADTH FIRST SEARCH
    '''

    def updateMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        rows, cols = len(matrix), len(matrix[0])

        # Prepare an answer matrix with the same dimensions
        distance_matrix = [[-1] * cols for _ in range(rows)]
        queue = deque()
      
        # Go through the matrix to find all the 0s
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # Set the distance for 0s as 0
                    distance_matrix[i][j] = 0
                    # Add the coordinates of the 0 to the queue
                    queue.append((i, j))
      
        while queue:
            i, j = queue.popleft()
            for dx, dy in self.directions:
                x, y = i + dx, j + dy
                
                is_inbound_neighbour = 0 <= x < rows and 0 <= y < cols
                # If the neighbor is within bounds and hasn't been visited
                if is_inbound_neighbour and distance_matrix[x][y] == -1:
                    # Update the distance for the neighbor
                    distance_matrix[x][y] = distance_matrix[i][j] + 1
                    # Add the neighbor's coordinates to the queue for further exploration
                    queue.append((x, y))
      
        return distance_matrix

    @property
    def directions(self):
        return ((-1, 0), (0, -1), (1, 0), (0, 1))


class Solution_V2:
    def updateMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        rows, cols = len(matrix), len(matrix[0])
        queue = deque()
      
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][j] = 0
                    queue.append((i, j))
                else:
                    matrix[i][j] = '#'
      
        while queue:
            i, j = queue.popleft()
            for dx, dy in self.directions:
                x, y = i + dx, j + dy
                
                is_inbound_neighbour = 0 <= x < rows and 0 <= y < cols
                if is_inbound_neighbour and matrix[x][y] == '#':
                    matrix[x][y] = matrix[i][j] + 1
                    queue.append((x, y))
      
        return matrix

    @property
    def directions(self):
        return ((-1, 0), (0, -1), (1, 0), (0, 1))
