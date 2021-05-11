def fib(n):
    dp = [0] * n
    dp[0], dp[1] = 0, 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


print(fib(10))

# RECURSION


def fibonacci(n):
    '''O(2^n)) -> Exponential'''
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# MEMOIZATION


def fib_memoized(n, memo={}):
    '''Time - O(n), Space - O(n)'''

    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fib_memoized(n - 1) + fib_memoized(n - 2)
    return memo[n]

# ITERATION


def fib_iter(n):
    ''' O(n) time and O(1) space.'''

    if n < 0:
        raise IndexError('Negative Index 🌜')
    if n <= 1:
        return 1

    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr

    return prev
