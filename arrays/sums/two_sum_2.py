'''
167. Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be 
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]

Example 2:
Input: numbers = [2, 3, 4], target = 6
Output: [1, 3]
'''


def twoSum(nums, target):
    dic = {}

    for i, num in enumerate(nums):
        rem = target-num

        if rem in dic:
            return [dic[rem] + 1, i + 1]

        dic[num] = i


def twoSum_v2(nums, target):
    l, r = 0, len(nums)-1

    while l < r:
        s = nums[l] + nums[r]

        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1
