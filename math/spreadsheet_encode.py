'''
171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/description/

Given a string columnTitle that represents the column title as appears in an Excel sheet, 
return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Examples:
1. 'A' -> 1
2. 'AB' -> 28
3. 'ZY' -> 701

INTUITION
AB -> (1 * 26 ^ 1) + (2 * 26 ^ 0) = 28
ZY -> (26 * 26 ^ 1) + (25 * 26 ^ 0) = 701
BBC -> (2 * 26 ^ 2) + (2 * 26 ^ 1) + (3 * 26 ^ 0) = 1407
'''

import string

def titleToNumber(columnTitle: str) -> int:
    result = 0
    for i, ch in enumerate(reversed(columnTitle)):
        curr_num = ord(ch) - ord('A') + 1
        result += curr_num * (26 ** i)

    return result

def titleToNumberV2(columnTitle: str) -> int:
    letters = string.ascii_uppercase
    numbers = range(1, 27)
    mapping = dict(zip(letters, numbers))

    result = 0
    for i, ch in enumerate(reversed(columnTitle)):
        curr_num = mapping[ch]
        result += curr_num * (26 ** i)

    return result

