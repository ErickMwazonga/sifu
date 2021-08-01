'''
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/
CREDIT: https://www.youtube.com/watch?v=yzB4M-UXqgI

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

ExampleS:
Input: num = 3 -> "III"
Input: num = 4 -> "IV"
Input: num = 9 -> "IX"
Input: num = 58 -> "LVIII"
    Explanation: L = 50, V = 5, III = 3.
Input: num = 1994 -> "MCMXCIV"
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        mapping = self.mapping()

        # The dictionary loop doesn't affect time complexity since it doesn't change
        for roman, value in mapping.items():
            no_of_symbols = num // value

            if no_of_symbols > 0:
                result += roman * no_of_symbols

            num %= value

        return result

    def mapping(self):
        # edge_cases = 4, 9, 10, 90, 400, 900

        _hash = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }

        return _hash


soln = Solution()

assert soln.intToRoman(3) == "III"
assert soln.intToRoman(4) == "IV"
assert soln.intToRoman(9) == "IX"
assert soln.intToRoman(58) == "LVIII"
assert soln.intToRoman(1994) == "MCMXCIV"
