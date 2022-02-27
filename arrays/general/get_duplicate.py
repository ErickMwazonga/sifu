'''
Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.
'''


def get_duplicate(A):
    '''Time: O(1)'''

    n = len(A) - 1
    total = n * (n + 1) // 2

    sum_of_A = sum(A)

    return sum_of_A - total


assert get_duplicate([1, 3, 4, 2, 2]) == 2
assert get_duplicate([1, 2, 4, 3, 3]) == 3
