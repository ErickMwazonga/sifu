'''
167. Two Sum II - Input array is sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they
add up to the target, where index1 must be less than index2.

Example 1:
Input: numbers = [2, 7, 11, 15],  target = 9 -> [1, 2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2, 3, 4], target = 6 -> [1, 3]
'''


def twoSum(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        _sum = nums[low] + nums[high]

        if _sum == target:
            return [low + 1, high + 1]
        elif _sum < target:
            low += 1
        else:
            high -= 1

    return []


assert sorted(twoSum([2, 7, 11, 15], 9)) == sorted([0, 1])
assert sorted(twoSum([2, 6, 11, 7, 15], 9)) == sorted([0, 3])
