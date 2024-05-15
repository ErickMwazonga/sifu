from typing import Dict
from functools import lru_cache

'''
Intuition
fib(n) = fib(n-1) + fib(n-2) for n > 2
'''


def fibonacci(n):
    '''Time - O(2^n)) -> Exponential, Space - O(n) -> Storage of call stack'''

    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# MEMOIZATION - Maintain a CACHE
def fibonacci_memo(n: int) -> int:
    '''Time - O(n), Space - O(n)'''

    memo: Dict[int, int] = {0: 0, 1: 1}

    if n not in memo:
        memo[n] = memo[n-1] + memo[n-2]  # memoization

    return memo[n]


def fib_memoized(n, memo={0: 0, 1: 1}):
    '''Time - O(n), Space - O(n)'''

    if n in memo:
        return memo[n]

    memo[n] = fib_memoized(n-1, memo) + fib_memoized(n-2, memo)
    return memo[n]


@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    if n <= 1:
        return 1

    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


def fib(n):
    dp = [0] * n
    dp[0], dp[1] = 0, 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


def fib_v2(n):
    if n < 1:
        return -1

    if n == 1:
        return 1

    prev, curr = 0, 1

    for _ in range(1, n):
        fib = prev + curr
        prev, curr = curr, fib

    return curr


def fib_v3(n: int) -> int:
    '''Time - O(n), Space - O(1)'''

    if n == 0:
        return n

    last: int = 0
    _next: int = 1

    for _ in range(1, n):
        last, _next = _next, last + _next

    return _next
