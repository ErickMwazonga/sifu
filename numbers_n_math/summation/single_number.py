'''
136. Single Number
https://leetcode.com/problems/find-the-duplicate-number/submissions/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Examples:
1. [2,2,1] ->  1
2. [4,1,2,1,2] -> 4
3. [1] -> 1
'''


def singleNumber(nums):
    frequency = {}

    for i in nums:
        frequency[i] = frequency.get(i, 0) + 1

    for i in frequency:
        if frequency[i] == 1:
            return i


def singleNumber(nums):
    '''Formula: 2*(a+b+c) - (a+a+b+b+c) = c'''

    return 2 * sum(set(nums)) - sum(nums)
