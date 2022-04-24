'''
7. Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Examples:
1. 123 -> 321
2. -123 -> -321
3. 120 -> 21
4. 0 -> 0
'''


def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1

    x = abs(x)
    reversed_x = 0

    while x > 0:
        x, rem = divmod(x, 10)
        reversed_x = (reversed_x * 10) + rem

    return reversed_x * sign


assert reverse(123) == 321
assert reverse(-123) == -321
assert reverse(120) == 21
assert reverse(0) == 0
