'''
665 Non-decreasing Array
Link: https://leetcode.com/problems/non-decreasing-array/

Given an array nums with n integers, your task is to check if it
could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1]
olds for every i (0-based) such that (0 <= i <= n - 2).

Examples:
1. [4, 2, 3] -> True => You could modify the first 4 to 1 to get a non-decreasing array.
2. [4, 2, 1] -> False => You can't get a non-decreasing array by modify at most one element.
'''


def check_possibility(nums):
    changed = False

    for i in range(0, len(nums)-1):
        if nums[i] > nums[i + 1]:
            if changed:
                return False

            if i != 0 and (nums[i - 1] > nums[i + 1]):
                nums[i + 1] = nums[i]

            changed = True

    return True


def check_possibility_v2(nums):
    count = 0
    n = len(nums)

    if n <= 2:
        return True

    for i in range(0, n-1):
        if nums[i] > nums[i+1]:
            count += 1

            if count > 1:
                return False

            if (i-1) >= 0 and nums[i-1] > nums[i+1]:
                nums[i+1] = nums[i]

    return True
