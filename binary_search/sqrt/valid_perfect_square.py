'''
367. Valid Perfect Square
Link: https://leetcode.com/problems/valid-perfect-square/
Related: L69, L633

Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Examples:
1. 16 -> True
2. 14 -> False
'''


def isPerfectSquare(num):
    '''Time: O(sqrt(n))'''

    for i in range(1, num + 1):
        if i * i == num:
            return True

        if i * i > num:
            return False


def isPerfectSquare_v2(num):
    '''Time: O(logn)'''

    left, right = 1, num

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False
