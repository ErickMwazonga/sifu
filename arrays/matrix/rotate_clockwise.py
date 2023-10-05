'''
48. Rotate Image
Link: https://leetcode.com/problems/rotate-image/
# C L O C K W I S E

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you
have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
'''


class Solution:

    def rotate_final(self, matrix):
        # Two steps: reverse and transpose in place
        matrix.reverse()

        # Transpose
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(i+1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def transpose(self, matrix):
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(i+1, m):  # Items less than i have already been transposed
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix

    def rotate(self, matrix):
        matrix.reverse()
        self.transpose(matrix)


s = Solution()
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s.rotate(m) == [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
