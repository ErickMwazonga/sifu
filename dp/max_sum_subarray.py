'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
Follow up: If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4] -> 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1] -> 1
Input: nums = [0] -> 0
Input: nums = [-1] -> -1
Input: nums = [-2147483647] -> -2147483647
Input: arr = [2, 3, -6, 4, 2, -8, 3] -> 6
    Explanation: the maximum subarray is [4, 2], its sum is 6
Input: arr = [2, 3, -1, 4, -10, 2, 5] -> 8
    Explanation: the maximum subarray is [2, 3, -1, 4], its sum is 8
Input: arr = [-3, -1, -2] -> Output: -1
    Explanation: the maximum subarray is [-1], its sum is -1
'''

# Kadane’s algorithm


def maxSubArray(nums: list) -> int:
    curr_sum = max_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum


def max_subarray(A):
    max_ending_here = max_so_far = A[0]

    for num in A[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray([5, 4, -1, 7, 8]) == 23
assert max_subarray([1]) == 1
