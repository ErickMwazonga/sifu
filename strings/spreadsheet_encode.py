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
    
Examples:
1. 'A' -> 1
2. 'AB' -> 28
3. 'ZY' -> 701
'''


class Solution:
    '''
    e.g
    AA
    (A * 26^1 + A * 26^0)
    '''

    def titleToNumber(self, s: str) -> int:
        num = 0
        exp = len(s) - 1

        for char in s:
            val = self.mapping(char) * (26 ** exp)
            num += val
            exp -= 1

        return num

    def mapping(self, char):
        return ord(char) - ord('A') + 1


soln = Solution()
assert soln.titleToNumber('A') == 1
assert soln.titleToNumber('AB') == 28
assert soln.titleToNumber('ZY') == 701
