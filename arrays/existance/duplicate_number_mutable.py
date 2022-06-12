'''
287. Find the Duplicate Number
Link: https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Examples
1. [1, 3, 4, 2, 2, 2] -> 2
2. [3, 1, 3, 3, 4, 2] -> 3
'''


def findDuplicate(nums):
    for num in nums:
        abs_num = abs(num)

        if nums[abs_num] < 0:
            return abs_num

        nums[abs_num] = -nums[abs_num]


def findDuplicate_v2(A):
    n = len(A)

    for i in range(n+1):
        val_index = abs(A[i])

        if A[val_index] < 0:
            return val_index

        A[val_index] = -A[val_index]


assert findDuplicate([1, 3, 4, 2, 2]) == 2
assert findDuplicate([1, 2, 4, 3, 3]) == 3
