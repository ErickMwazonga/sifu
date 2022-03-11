'''
442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Given an integer array nums of length n where all the integers of nums are in the range [1, n]
and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Examples:
1. [4, 3, 2, 7, 8, 2, 3, 1] -> [2, 3]
2. [1, 1, 2] -> [1]
3. [1] -> []
'''


def findDuplicates(nums):
    freqs = {}

    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1

    res = []
    for k, v in freqs.items():
        if v == 2:
            res.append(k)

    return res


def findDuplicates1(nums):
    res = []

    for num in nums:
        index = abs(num) - 1

        if nums[index] < 0:
            res.append(index + 1)

        nums[index] = -nums[index]

    return res
