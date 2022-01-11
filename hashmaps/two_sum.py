"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums: list, target: int) -> list:
    '''
    Time complexity: 0(n) where n is the length of nums
    '''
    seen = {}

    for key, value in enumerate(nums):
        rem = target - value
        if rem in seen:
            return [key, seen[rem]]
        seen[value] = key


assert sorted(twoSum([2, 7, 11, 15], 9)) == sorted([0, 1])
assert sorted(twoSum([2, 6, 11, 7, 15], 9)) == sorted([0, 3])


def two_sum_brute_force(A, target):
    '''Time Complexity: O(n^2), Space Complexity: O(1)'''

    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True

    return False
