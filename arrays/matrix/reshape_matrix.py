'''
566. Reshape the Matrix
Link: https://leetcode.com/problems/reshape-the-matrix/

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix
into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and
the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; 4
Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
'''


def matrixReshape(matrix, r, c):
    if not matrix:
        return matrix

    flattened = sum(matrix, [])

    if r * c > len(flattened):
        return matrix

    results = []

    index = 0
    for i in range(r):
        results.append([])

        for _ in range(c):
            curr_num = flattened[index]
            results[i].append(curr_num)
            index += 1

    return results


def matrixReshape_v2(mat, r: int, c: int):
    if not mat:
        return mat

    n, m = len(mat), len(mat[0])

    if n * m != r * c:
        return mat

    new_mat = [[0 for _ in range(c)] for _ in range(r)]

    i = 0
    while i < r * c:
        old_row, old_col = divmod(i, m)
        new_row, new_col = divmod(i, c)

        new_mat[new_row][new_col] = mat[old_row][old_col]
        i += 1

    return new_mat
