'''
498. Diagonal Traverse
https://leetcode.com/problems/diagonal-traverse/
https://leetcode.com/problems/diagonal-traverse/discuss/145195/python-solution-beats-100-using-bfs-just-like-maze-problem

Given a matrix of M x N elements (M rows, N columns),
return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation: visit link
'''

from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
		## TIME COMPLEXITY : O(MxN) ##
		## SPACE COMPLEXITY : O(MxN) ##

        if not matrix:
            return []

        n, m = len(matrix), len(matrix[0])
        diagonals = defaultdict(list)

        for i in range(n):
            for j in range(m):
                diagonals[i+j].append(matrix[i][j])

        res = []
        for i, d in enumerate(diagonals.values()):
            if i % 2 != 1:
                res.extend(d)
            else:
                res.extend(d[::-1])

        return res