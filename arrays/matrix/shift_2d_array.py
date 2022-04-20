'''
1260. Shift 2D Grid
https://leetcode.com/problems/shift-2d-grid/

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:
Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
'''


def shiftGrid(grid, k: int):
    m, n = len(grid), len(grid[0])
    tot_len = m * n

    # new grid
    new_grid = [[0 for i in range(n)] for j in range(m)]

    for i in range(tot_len):
        old_row_index, old_column_index = divmod(i, n)

        new_linear_index = (i + k) % tot_len
        new_row_index, new_column_index = divmod(new_linear_index, n)

        new_grid[new_row_index][new_column_index] = grid[old_row_index][old_column_index]

    return new_grid
