from typing import Dict
from functools import lru_cache


def fibonacci(n):
    '''O(2^n)) -> Exponential'''

    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n: int) -> int:
    memo: Dict[int: int] = {0: 0, 1: 1}

    if n not in memo:
        memo[n] = memo[n-1] + memo[n-2]  # memoization

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


def fib2(n):
    if n < 1:
        return -1

    if n == 1:
        return 1

    prev, curr = 0, 1

    for _ in range(1, n):
        fib = prev + curr
        prev, curr = curr, fib

    return curr


def fib5(n: int) -> int:
    if n == 0:
        return n

    last: int = 0
    _next: int = 1

    for _ in range(1, n):
        last, _next = _next, last + _next

    return _next
