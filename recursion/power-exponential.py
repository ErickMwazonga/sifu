'''
Implement integer exponentiation.
That is, implement the power(x, y) function,
where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.
'''


def power(x, n):
    '''Time O(log n)'''
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = power(x, n/2)
        return y * y
    else:
        return x * power(x, n-1)


assert power(2, 0) == 1
assert power(2, 3) == 8
assert power(2, 4) == 16
assert power(2, 10) == 1024
