'''
50. Pow(x, n)
Link: https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.00000, n = -2
Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25
'''


def myPow(x, n):
    '''Time: O(n)'''
    if n == 0:
        return 1

    if n == 1:
        return x

    is_nengative = n < 0
    n = abs(n)

    res = x
    i = 1
    while i < n:
        res *= x
        i += 1

    return 1 / res if is_nengative else res


def myPow_v2(x, n):
    '''
    Time O(log n) - 2^4 -> 2^2 * 2^2 
    e.g 2^8
    n | [n // 2] 8 4 2  1
    x | [x ** 2] 2 4 16 256
    '''

    if n == 0:
        return 1

    if n == 1:
        return x

    is_negative = n < 0
    n = abs(n)

    res = 1
    while n:
        is_odd = n % 2

        if is_odd:
            n -= 1
            res = res * x
        else:
            n //= 2
            x = x * x  # x = x ** 2

    return 1 / res if is_negative else res


def myPow_v3(x: float, n: int) -> float:
    '''Time O(log n) - 2^4 -> 2^2 * 2^2 - Account for negatives'''

    is_negative = n < 0
    n = abs(n)

    if x == 0 or x == 1:
        return x

    if n % 2 == 0:
        y = pow(x, n/2)
        result = y * y
    else:
        result = x * pow(x, n-1)

    return 1 / result if is_negative else result


assert pow(2, 0) == 1
assert pow(2, 3) == 8
assert pow(2, -3) == 1/8
assert pow(2, 4) == 16
assert pow(2, 10) == 1024
