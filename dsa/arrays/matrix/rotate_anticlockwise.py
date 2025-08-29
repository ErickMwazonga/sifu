'''
Rotate Image A N T I C L O C K W I S E
'''


class Solution:

    def transpose(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def rotate(self, matrix):
        # Two steps: reverse items and transpose in place
        for row in matrix:
            row.reverse()

        self.transpose(matrix)


s = Solution()
m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

output = [[3, 6, 9],
          [2, 5, 8],
          [1, 4, 7]]

assert s.rotate(m) == output
