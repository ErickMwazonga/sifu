'''
171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A" -> 1
Input: "AB" -> 28
Input: "ZY" -> 701
'''

class Solution:
    '''
    e.g
    AA
    (A * 26^1 + A * 26^0)
    '''

    def titleToNumber(self, s: str) -> int:
        num = 0
        count = len(s) - 1
        
        for char in s:
            num += self.mapping(char) * (26 ** count)
            count -= 1
        
        return num
        
    def mapping(self, char):
        return ord(char) - ord('A') + 1


print(spreadsheet_encode_column("ZZ"))