'''
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Examples
1. [1, 3, 4, 2, 2, 2] -> 2
2. [3, 1, 3, 3, 4, 2] -> 3
'''


def findDuplicate(nums):
    d = {}
    for each in nums:
        if each in d:
            return each
        else:
            d[each] = 1


def findDuplicate1(nums):
    nums_set = set()
    for num in nums:
        if num in nums_set:
            return num

        nums_set.add(num)


def findDuplicate2(nums):
    for v in nums:
        pos = abs(v) - 1

        if nums[pos] < 0:
            return pos + 1

        nums[pos] = -nums[pos]


assert findDuplicate([1, 3, 4, 2, 2]) == 2
assert findDuplicate([1, 2, 4, 3, 3]) == 3
