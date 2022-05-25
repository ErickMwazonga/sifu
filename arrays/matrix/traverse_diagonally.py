'''
498. Diagonal Traverse
Link: https://leetcode.com/problems/diagonal-traverse/
Credit: https://bit.ly/3yTBnwZ

Given a matrix of M x N elements (M rows, N columns),
return all elements of the matrix in diagonal order as shown in the below image.

Example:
[[ 1, 2, 3 ],
 [ 4, 5, 6 ],    --> [1, 2, 4, 7, 5, 3, 6, 8, 9]
 [ 7, 8, 9 ]] 
'''

from collections import defaultdict


class Solution:
    def find_diagonal_order(self, matrix):
        if not matrix:
            return matrix

        n, m = len(matrix), len(matrix[0])
        diagonals = defaultdict(list)

        # Build diagonals
        for i in range(n):
            for j in range(m):
                diagonals[i+j].append(matrix[i][j])

        res = []
        # Get values in respective order
        for k, diagonal in diagonals.items():
            if k % 2 == 0:
                res.extend(diagonal[::-1])
            else:
                res.extend(diagonal)

        return res

    def find_diagonal_order_one_directional(self, matrix):
        if not matrix:
            return []

        n, m = len(matrix), len(matrix[0])
        diagonals = defaultdict(list)

        for i in range(n):
            for j in range(m):
                diagonals[i+j].append(matrix[i][j])

        return list(diagonals.values())


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
output = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]

soln = Solution()
assert soln.find_diagonal_order(matrix) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
assert soln.find_diagonal_order_one_directional(matrix) == output
