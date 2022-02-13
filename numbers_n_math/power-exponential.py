'''
Implement integer exponentiation.
That is, implement the power(x, y) function,
where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.
'''


def power(x, n):
    '''Time O(log n) - 2^4 -> 2^2 * z^2
    # Account for negatives
    '''

    is_negative = True if n < 0 else False
    n = abs(n)

    if x == 0:
        return 0
    elif n == 0:
        return 1

    if n % 2 == 0:
        y = power(x, n/2)
        result = y * y
    else:
        result = x * power(x, n-1)

    return 1 / result if is_negative else result


assert power(2, 0) == 1
assert power(2, 3) == 8
assert power(2, -3) == 1/8
assert power(2, 4) == 16
assert power(2, 10) == 1024
