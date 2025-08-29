'''
6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
 
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
'''

from collections import defaultdict

def convert_v1(s: str, numRows: int) -> str:
    mapping = defaultdict(str)
    curr_line = 0
    direction = 1  # 1 for moving forward, -1 for moving backward

    for ch in s:
        mapping[curr_line] += ch

        if direction == 1:
            if curr_line < numRows - 1:
                curr_line += 1
            else:
                direction = -1
                curr_line -= 1
        else:
            if curr_line > 0:
                curr_line -= 1
            else:
                direction = 1
                curr_line += 1

    return ''.join(mapping.values())


def convert_v2(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    zigzag_lines = [''] * numRows
    curr_line = 0
    direction = 1  # 1 for moving forward, -1 for moving backward

    for ch in s:
        zigzag_lines[curr_line] += ch
        curr_line += direction
        if curr_line == 0 or curr_line == numRows - 1:
            direction *= -1

    return ''.join(zigzag_lines)