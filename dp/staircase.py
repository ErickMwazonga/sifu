'''
Climbing Stairs -> FIBONACCI
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


def staircase(n, X):
    '''
    This now takes O(N * |X|) time and O(N) space
    https://www.dailycodingproblem.com/blog/staircase-problem/
    '''
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x > 0)
        cache[i] += 1 if i in X else 0
    return cache[-1]


def climb_stairs(n: int) -> int:
    '''Time – O(n), space: O(n)'''
    memo = {}

    def helper(n):
        if (n <= 2):
            return n
        elif n in memo:
            return memo[n]
        else:
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]

    return helper(n)


assert climb_stairs(5) == 8
assert climb_stairs(6) == 13
assert climb_stairs(7) == 21


# FIBONACCI
def fib(n):
    dp = [0] * n

    for i in range(n):
        if i <= 2:
            dp[i] = i + 1
        else:
            dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


assert fib(5) == 8
assert fib(6) == 13
assert fib(7) == 21
