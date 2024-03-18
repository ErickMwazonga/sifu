'''
136. Single Number
https://leetcode.com/problems/single-number/description/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Examples:
1. [2, 2, 1] ->  1
2. [4, 1, 2, 1, 2] -> 4
3. [1] -> 1
'''

from functools import reduce


def single_number(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

def single_number_v2(nums: list[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)