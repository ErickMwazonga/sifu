import functools


def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        # key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


fibonacci(10)
