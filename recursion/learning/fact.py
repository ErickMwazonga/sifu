# Calculate the factorial of a given number n.

def fact(n: int) -> int:
    if n == 1:
        return 1
    return n * fact(n - 1)

assert fact(3) == 6