'''
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Examples:
Input: x = 123 -> 321
Input: x = -123 -> -321
Input: x = 120 -> 21
Input: x = 0 -> 0
'''


def reverse(x: int) -> int:
    is_negative = x < 0

    x = abs(x)
    reversed_x = 0

    while x > 0:
        x, rem = divmod(x, 10)
        reversed_x = (reversed_x * 10) + rem

    if is_negative:
        return -reversed_x

    return reversed_x


assert reverse(123) == 321
assert reverse(-123) == -321
assert reverse(120) == 21
assert reverse(0) == 0
