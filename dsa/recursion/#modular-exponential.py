'''
Modular Exponentiation (Power in Modular Arithmetic)
Given three numbers x, y and p, compute (xy) % p.

Examples :
Input:  x = 2, y = 3, p = 5
Output: 3
Explanation: 2^3 % 5 = 8 % 5 = 3.

Input:  x = 2, y = 5, p = 13
Output: 6
Explanation: 2^5 % 13 = 32 % 13 = 6.
'''


def mod(x, n, m):
    '''
    (a * b) % m = ((a % m) * (b % m)) % m
    Time O(log n)
    '''

    if n == 0:
        return 1

    if n % 2 == 0:
        y = mod(x, n/2, m)
        return (y * y) % m

    return (((x % m) * mod(x, n-1, m)) % m)


assert mod(2, 3, 5) == 3
assert mod(2, 5, 13) == 6
