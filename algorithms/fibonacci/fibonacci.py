'''
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
Examples:
2 -> 1 => Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
3 -> 2 => Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
4 -> 3 => Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
'''


def fibonacci(n):
    '''O(2^n)) -> Exponential'''

    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_memoized(n, memo={}):
    '''Time - O(n), Space - O(n)'''

    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fib_memoized(n - 1) + fib_memoized(n - 2)
    return memo[n]


def fib(n):
    dp = [0] * n
    dp[0], dp[1] = 0, 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


def fib_iter(n):
    '''Time - O(n), Space - O(1)'''

    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr

    return prev


assert fib_iter(5) == 5
assert fib_iter(6) == 8
assert fib_iter(7) == 13
