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
    seen = {}

    for each in nums:
        if each in seen:
            return each
        else:
            seen[each] = 1


def findDuplicate_v1(nums):
    nums_set = set()

    for num in nums:
        if num in nums_set:
            return num

        nums_set.add(num)


def findDuplicate_v2(nums):
    for v in nums:
        pos = abs(v) - 1

        if nums[pos] < 0:
            return pos + 1

        nums[pos] = -nums[pos]


def findDuplicate_v3(A):
    n = len(A)

    for i in range(n+1):
        val_index = abs(A[i])

        if A[val_index] < 0:
            return val_index

        A[val_index] = -A[val_index]


assert findDuplicate([1, 3, 4, 2, 2]) == 2
assert findDuplicate([1, 2, 4, 3, 3]) == 3
