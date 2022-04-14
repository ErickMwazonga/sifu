'''
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
'''


def pow(x: float, n: int) -> float:
    '''Time O(log n) - 2^4 -> 2^2 * z^2 - Account for negatives'''

    is_negative = True if n < 0 else False
    n = abs(n)

    if x == 0 or x == 1:
        return x

    if n % 2 == 0:
        y = pow(x, n/2)
        result = y * y
    else:
        result = x * pow(x, n-1)

    return 1 / result if is_negative else result


def myPow(x: float, n: int) -> float:
    memo = {}

    def power(x, n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            memo[n] = power(1/x, -n)
            return memo[n]
        elif n % 2 == 0:
            memo[n] = power(x*x, n//2)
            return memo[n]
        else:
            memo[n] = x * power(x*x, (n-1)//2)
            return memo[n]

    return power(x, n)


assert pow(2, 0) == 1
assert pow(2, 3) == 8
assert pow(2, -3) == 1/8
assert pow(2, 4) == 16
assert pow(2, 10) == 1024
