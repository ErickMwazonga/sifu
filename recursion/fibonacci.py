def fibonacci(n):
    '''O(2^n)) -> Exponential'''
    
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fib(n):
    dp = [0] * n
    dp[0], dp[1] = 0, 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]