"""
Check Whether a Number is Palindrome or Not

Time complexity : O(log 10(n)).
We divided the input by 10 for every iteration,
so the time complexity is O(log10(n))

Space complexity : O(1)
"""

def is_palindrome(num):
    original_num = num
    reversed_num = 0
    
    while(num != 0):
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num //= 10
    
    if original_num == reversed_num:
        return True
    else:
        return False


assert is_palindrome(121) == True
assert is_palindrome(1212) == False