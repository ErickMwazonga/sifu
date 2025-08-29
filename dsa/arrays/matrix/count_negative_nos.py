'''
1351. Count Negative Numbers in a Sorted Matrix
Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/submissions/

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
Return the number of negative numbers in grid.

Examples
[[4,  3,   2, -1],
 [3,  2,   1, -1],     ---> 8
 [1,  1,  -1, -2],
 [-1, -1, -2, -3]]

[[3, 2],     ---> 0
 [1, 0]]

[[ 1, -1],   ---> 3
 [-1, -1]]

[[-1]]    ---> 1
'''


def countNegatives(grid):
    grid_list = sum(grid, [])
    return len([i for i in grid_list if i < 0])


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


class Solution():

    def search(self, arr):
        low, high = 0, len(arr)

        while low < high:
            mid = (low + high) // 2

            if arr[mid] >= 0:
                low = mid + 1
            else:
                high = mid

        # To find the count of negative numbers
        return len(arr) - high

    def countNegatives(self, grid):
        count = 0

        for row in grid:
            count += self.search(row)

        return count
