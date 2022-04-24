'''
8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/
 
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
The algorithm for myAtoi(string s) is as follows:

Examples:
1. '123' -> 123
2. '-12332' -> -12332
3. '554' -> 554
'''


def myAtoi(_str):
    if not _str:
        return 0

    res = 0

    # whitespaces
    _str = _str.strip()

    # handle signs +/-
    sign = -1 if _str[0] == '-' else 1
    is_negative = sign == -1

    # starts with charactes
    if not _str[0].isnumeric() and _str[0] not in '-+':
        return 0

    start = 1 if is_negative else 0
    for i in range(start, len(_str)):
        if _str[i].isnumeric():
            val = ord(_str[i]) - ord('0')
            res = (res * 10) + val  # 45 = (4 * 10) + 5

    return res * sign


assert myAtoi('554') == 554
assert myAtoi('-994') == -994
assert myAtoi('4193 with words') == 4193
assert myAtoi('Word 345') == 0
assert myAtoi('     -42') == -42
