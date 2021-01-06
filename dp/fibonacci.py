def fib(n):
    dp = [0] * n
    dp[0], dp[1] = 0, 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]
    
print(fib(10))

def fibonacci(n):
    '''O(2^n)) -> Exponential'''
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibber(n):
    '''Time - O(n), Space - O(n)'''
    memo = {}

    def fib(n):
        if n < 0:
            raise IndexError('Negative Index 🌜')
        if n <= 1:
            return 1

        if n in memo:
            return memo[n]

        result = fib(n - 1) + fib(n - 2)
        memo[n] = result  # Memoize

        return result

    return fib(n)


  def fib(n):
    ''' O(n) time and O(1) space.'''

    if n < 0:
        raise IndexError('Negative Index 🌜')
    if n <= 1:
        return 1

    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr
    return prev

