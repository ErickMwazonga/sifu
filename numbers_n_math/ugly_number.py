'''
263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Example 1:
Input: n = 6 -> true
Explanation: 6 = 2 x 3

Example 2:
Input: n = 1 -> true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14 -> false
Explanation: 14 is not ugly since it includes the prime factor 7.
'''


def isUgly(num: int) -> bool:

    if num <= 0:
        return False

    primes = [2, 3, 5]
    for prime in primes:
        while num % prime == 0:
            num //= prime

    return num == 1


assert isUgly(6) == True
assert isUgly(1) == True
assert isUgly(14) == False
