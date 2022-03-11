'''
633. Sum of Square Numbers
Link: https://leetcode.com/problems/sum-of-square-numbers/
Related: L69, L367

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Examples:
1. 5 -> True | Explanation: 1 * 1 + 2 * 2 = 5
2. 3 -> False
'''


def judgeSquareSum(c):
    '''Time : O(sqrt(c)), Space: O(1)'''

    left, right = 0, int(c ** 0.5)

    while left <= right:
        powsum = left ** 2 + right ** 2

        if powsum == c:
            return True
        elif powsum > c:
            right -= 1
        else:
            left += 1

    return False
