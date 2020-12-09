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
'''

def maxSubArray(nums: List[int]) -> int:
    curr_sum, max_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    
    return max_sum


 def maxSubArray(nums: List[int]) -> int:
    if not nums:
        return 0
    
    summed = 0
    n = len(nums)
    solutions = [0] * n

    for i, val in enumerate(nums):
        if summed < 0:
            summed = 0

        summed += val
        solutions[i] = summed
    
    return max(solutions)