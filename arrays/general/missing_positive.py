'''
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array, find the smallest missing positive integer.
Example 1:

Input: [1,2,0] -> 3
Input: [3,4,-1,1] ->  2
Input: [7,8,9,11,12] -> 1

Your algorithm should run in O(n) time and uses constant extra space.
the additional space depends on your implementation.
But the time complexity is O(n), because membership check in a set is O(1)
and the for loop complexity is O(n) (same for array to set()).
therefore the overall asymptotic time complexity is O(n).
'''


def first_missing_postive(arr):
    visisted = set(arr)

    for i in range(1, len(arr) + 2):
        if i not in visisted:
            return i


def firstMissingPositive(nums) -> int:
    n = len(nums)

    # cleaning up the array (negative nos + nos > n)
    for idx in range(n):
        if nums[idx] <= 0 or nums[idx] > n:
            nums[idx] = n + 1

    # placing our marker to see what numbers have been accounted for
    for num in nums:
        num = abs(num)
        if num <= n and nums[num - 1] >= 0:
            nums[num - 1] *= -1

    # final step for getting the answer
    for idx in range(n):
        if nums[idx] > 0:
            return idx + 1

    return n + 1
