'''
9. Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.

Examples:
1. 121 -> true
2. -121 -> false
3. 10 -> false
'''


def is_palindrome(num):
    if num < 0:
        return False

    original_num = num
    reversed_num = 0

    while num != 0:
        num, rem = divmod(num, 10)
        reversed_num = (reversed_num * 10) + rem

    return original_num == reversed_num


assert is_palindrome(-23) == False
assert is_palindrome(0) == True
assert is_palindrome(121) == True
assert is_palindrome(1212) == False
