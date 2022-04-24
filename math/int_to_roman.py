'''
12. Integer to Roman
Link: https://leetcode.com/problems/integer-to-roman/
Credit: https://www.youtube.com/watch?v=yzB4M-UXqgI

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

Examples:
1. 3 -> 'III'
2. 4 -> 'IV'
3. 9 -> 'IX'
4. 58 -> 'LVIII'
    Explanation: L = 50, V = 5, III = 3.
5. 1994 -> 'MCMXCIV'
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


def intToRoman(num: int) -> str:
    result = ''
    mapping = mapping()

    for roman, value in mapping.items():
        no_of_symbols, num = divmod(num, value)

        if no_of_symbols > 0:
            result += roman * no_of_symbols

    return result


def mapping():
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


assert intToRoman(3) == 'III'
assert intToRoman(4) == 'IV'
assert intToRoman(9) == 'IX'
assert intToRoman(58) == 'LVIII'
assert intToRoman(1994) == 'MCMXCIV'
