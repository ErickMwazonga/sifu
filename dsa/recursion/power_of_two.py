'''
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Examples:
1. 1 -> True: Explanation: 2 ^ 0 = 1
2. 16 -> True: Explanation: 24 = 16
3. 3 -> False
'''

def isPowerOfTwo(n: int) -> bool:
    if n == 1:
        return True
    if n == 0 or n % 2:
        return False
    return isPowerOfTwo(n // 2)