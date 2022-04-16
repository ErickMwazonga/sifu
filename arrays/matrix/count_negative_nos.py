'''
1351. Count Negative Numbers in a Sorted Matrix
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
Return the number of negative numbers in grid.

grid = [
    [4,3,2,-1],
    [3,2,1,-1],
    [1,1,-1,-2],
    [-1,-1,-2,-3]
] -> 8
grid = [
    [3,2],
    [1,0]
] -> 0
grid = [
    [1,-1],
    [-1,-1]
] -> 3
grid = [[-1]] -> 1
'''


def countNegativesDESC(grid):
    n, m = len(grid), len(grid[0])
    i, j = n - 1, 0
    count = 0

    while j < m and i >= 0:
        if grid[i][j] < 0:
            count += m - j
            i -= 1
        else:
            j += 1

    return count


def countNegativesASC(grid):
    n, m = len(grid), len(grid[0])
    i, j = 0, m - 1
    count = 0

    while j >= 0 and i < n:
        if grid[i][j] < 0:
            count += j + 1
            i += 1
        else:
            j -= 1

    return count
