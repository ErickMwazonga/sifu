'''
867. Transpose Matrix
https://leetcode.com/problems/transpose-matrix/
Credit: https://levelup.gitconnected.com/make-way-for-the-matrix-a-complete-guide-to-solving-2d-array-coding-problems-725096d122d9

Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
'''


def transpose(matrix):
    n, m = len(matrix), len(matrix[0])
    transposed = [[0] * n for _ in range(m)]
    # transposed = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]

    return transposed


def transpose2(matrix):
    # ONLY IF IT'S A SQUARE MATRIX IN-PLACE

    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        for j in range(i+1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix
