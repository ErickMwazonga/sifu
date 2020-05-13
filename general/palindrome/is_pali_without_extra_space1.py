"""
To check a number is palindrome or not without using any extra space
Given a number ‘n’ and our goal is to find out it is palindrome or not without using
any extra space. We can’t make a new copy of number .

Examples:
Input  : 2332 -> Output : Yes it is Palindrome.
original number = 2332 === reversed number = 2332
Both are same hence the number is palindrome.

Input :1111 -> Output :Yes it is Palindrome.
Input : 1234 -> Output : No not Palindrome.
"""


def isPalindrome(n):
    # Find the appropriate divisor to extract the leading digit
    divisor = 1
    while (n / divisor >= 10):
        divisor *= 10

    while (n != 0):
        leading = n // divisor
        trailing = n % 10

        # If first and last digit not same return false
        if (leading != trailing):
            return False

        # Removing the leading and trailing digit from number
        n = (n % divisor) // 10

        # Reducing divisor by a factor of 2 as 2 digits are dropped
        divisor = divisor / 100

    return True


assert is_palindrome(121) == True
assert is_palindrome(1212) == False
