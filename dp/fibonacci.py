def fib(n):
    dp = [0, 1]
    for i in range(2, len(n)):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

fib(5)