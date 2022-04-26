'''
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
            [1]
          [1,  1]
        [1,  2,  1]
     [1,   3,   3,   1]
  [1,   4,   6,   4,    1]

Example 1:
Input: numRows = 5
Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''


def generate(numRows):
    if numRows < 1:
        return []

    result = [[1]]
    for i in range(1, numRows):
        row = [1, 1]

        for j in range(1, i):
            left_above = result[i-1][j-1]
            right_above = result[i-1][j]
            row.insert(j, left_above + right_above)

        result.append(row)

    return result


def generate_v2(n):
    if n < 1:
        return [[]]

    res = [[1]]
    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            left, right = res[i-1][j-1], res[i-1][j]
            row.append(left+right)

        row.append(1)
        res.append(row)

    return res
