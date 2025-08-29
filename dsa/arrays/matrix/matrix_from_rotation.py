'''
1886. Determine Whether Matrix Can Be Obtained By Rotation
Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal 
to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:
Input: mat = [[0, 1], [1, 0]], target = [[1, 0], [0, 1]]
Output: True
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 3:
Input: mat = [[0,0,0], [0,1,0], [1,1,1]], target = [[1,1,1], [0,1,0], [0,0,0]]
Output: true

'''


class Solution:
    
    def findRotation(self, matrix, target):
        # return any(matrix == self.rotate90(matrix) for _ in range(10))
        for _ in range(4):
            if self.rotate90(matrix) == target:
                return True

        return False

    def transpose(self, matrix):
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(i+1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate90(self, matrix):
        matrix.reverse()
        self.transpose(matrix)

        return matrix
