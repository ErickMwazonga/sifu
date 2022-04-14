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
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''


def generate(numRows: int) -> list[list[int]]:
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
