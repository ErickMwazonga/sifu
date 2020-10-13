def fibonacci(n):
    '''O(2^n)) -> Exponential'''
    
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)