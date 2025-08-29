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

def reverse_v1(x: int) -> int:
    '''Time: O(N) Space: O(1)'''

    s = str(abs(x))
    reversed = int(s[::-1])
    return reversed if x > 0 else reversed * -1


def reverse_v2(x: int) -> int:
    '''Time: O(logN) Space: O(1)'''

    sign = -1 if x < 0 else 1
    x, reversed_x = abs(x), 0

    while x > 0:
        x, rem = divmod(x, 10)
        reversed_x = (reversed_x * 10) + rem

    return reversed_x * sign

def reverse_v3(x: int) -> int:
    '''Time: O(logN) Space: O(1)'''

    is_positive = x > 0
    x, reversed_x = abs(x), 0

    while x:
        base = len(str(x)) - 1
        x, rem = divmod(x, 10)
        reversed_x += rem * 10 ** base

    ans = reversed_x if is_positive else reversed_x * -1


assert reverse_v1(123) == 321
assert reverse_v1(-123) == -321
assert reverse_v1(120) == 21
assert reverse_v1(0) == 0
