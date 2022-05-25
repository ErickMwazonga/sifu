'''
119. Pascal's Triangle II
Link: https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
            [1]
          [1,  1]
        [1,  2,  1]
     [1,   3,   3,   1]
  [1,   4,   6,   4,    1]

Examples:
rowIndex = 3 -> [1,3,3,1]
rowIndex = 0 -> [1]
rowIndex = 1 -> [1,1]
'''


def getRow(rowIndex: int) -> list[int]:
    if rowIndex < 1:
        return []

    result = [[1]]
    for i in range(1, rowIndex+1):
        row = [1, 1]

        for j in range(1, i):
            left_above = result[i-1][j-1]
            right_above = result[i-1][j]
            row.insert(j, left_above + right_above)

        result.append(row)

    return result[-1]


def getRow_v2(n):
    if n == 0:
        return [1]

    res = [1]
    for i in range(1, n+1):
        curr_row = [1]

        for j in range(1, i):
            left, right = res[j-1], res[j]
            curr_row.append(left + right)

        curr_row.append(1)
        res = curr_row

    return curr_row
