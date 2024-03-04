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


def two_sum_v1(nums: list[int], target: int) -> list[int] | None:
    seen = {}

    for i, num in enumerate(nums):
        rem = target - num

        if rem in seen:
            return [seen[rem] + 1, i + 1]

        seen[num] = i


def two_sum_v2(nums: list[int], target: int) -> list[int] | None:
    left, right = 0, len(nums) - 1

    # It cannot be left <= right because we'll be adding the value against itself at the end
    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

print(two_sum_v2([2, 7, 11, 15], 9))
print(two_sum_v2([2, 3, 4], 6))

assert two_sum_v2([2, 7, 11, 15], 9) == [1, 2]
assert two_sum_v2([2, 3, 4], 6) == [1, 3]
