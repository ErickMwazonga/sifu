"""
Check Whether a Number is Palindrome or Not

Time complexity : O(log_{10}(n))O(log 10(n)).
We divided the input by 10 for every iteration,
so the time complexity is O(log_{10}(n))O(log10(n))

Space complexity : O(1)O(1).
"""

def is_palindrome(num):
    original_num = num
    reversed_num = 0
    
    while(num != 0):
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num //= 10
    
    if original_num == reversed_num:
        print(f'{num} is a palindrome')
    else:
        print(f'{num} is not a palindrome')


is_palindrome(121)
is_palindrome(1212)