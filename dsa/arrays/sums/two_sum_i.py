'''
1. Two Sum
Link: https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


def two_sum_v1(nums: list[int], target: int) -> list | None:
    '''Time: 0(n^2), Space: 0(1)'''

    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            rem = target - nums[i]
            if rem == nums[j]:
                return [i, j]


def two_sum_v2(nums: list, target: int) -> list | None:
    '''Time: 0(n), Space: 0(n)'''

    seen = {}

    for key, value in enumerate(nums):
        rem = target - value

        if rem in seen:
            return [key, seen[rem]]

        seen[value] = key


assert sorted(two_sum_v2([2, 7, 11, 15], 9)) == sorted([0, 1])
assert sorted(two_sum_v2([2, 6, 11, 7, 15], 9)) == sorted([0, 3])
