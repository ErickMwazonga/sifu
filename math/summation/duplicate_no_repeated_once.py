'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

[NOTE]: The repeated number is only repeated once

Examples
1. [1, 3, 4, 2] -> 2
2. [3, 1, 3, 4, 2] -> 3
'''


def get_duplicate(A):
    '''Time: O(1)'''

    n = len(A) - 1
    total = n * (n + 1) // 2

    sum_of_A = sum(A)

    return sum_of_A - total


assert get_duplicate([1, 3, 4, 2, 2]) == 2
assert get_duplicate([1, 2, 4, 3, 3]) == 3
