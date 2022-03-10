'''
69. Sqrt(x)
Problem Link: https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated
and only the integer part of the result is returned.

Write a function that takes a non-negative integer and returns
the largest integer whose square is less than or equal to
the integer given.
Example:
    Assume input is integer 300.
    Then the expected output of the function should be
    17, since 17^2 = 289 < 300. Note that 18^2 = 324 > 300,
    so the number 17 is the correct response.
'''


def integer_square_root(k):
    if k <= 1:
        return k

    low, high = 0, k

    while low < high:
        mid = low + (high - low) // 2
        mid_squared = mid * mid

        if mid_squared == k:
            return mid
        elif mid_squared < k:
            low = mid + 1
        else:
            high = mid

    return low - 1


def mySqrt(x: int) -> int:
    low, high = 0, x

    while low <= high:
        mid = low + (high - low) // 2
        mid_squared = mid ** 2

        if mid_squared <= x and (mid + 1) ** 2 > x:
            return mid
        elif mid_squared < x:
            low = mid + 1
        else:
            high = mid - 1

    return low


assert integer_square_root(300) == 17
assert integer_square_root(16) == 4
assert integer_square_root(17) == 4
