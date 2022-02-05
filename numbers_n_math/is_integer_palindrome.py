'''
Check Whether a Number is Palindrome or Not
https://leetcode.com/problems/palindrome-number/

Time complexity : O(log 10(n)).
We divided the input by 10 for every iteration,
so the time complexity is O(log10(n))

Space complexity : O(1)
'''


def is_palindrome(num):
    if num < 0:
        return False

    original_num = num
    reversed_num = 0

    while (num != 0):
        num, rem = divmod(num, 10)
        reversed_num = (reversed_num * 10) + rem

    return original_num == reversed_num


assert is_palindrome(-23) == False
assert is_palindrome(0) == True
assert is_palindrome(121) == True
assert is_palindrome(1212) == False
