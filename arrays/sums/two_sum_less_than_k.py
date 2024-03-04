'''
1099 - Two Sum Less Than K
https://leetcode.com/problems/two-sum-less-than-k/description/

Given an array nums of integers and integer k, 
return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. 
If no i, j exist satisfying this equation, return -1.

Example 1:
Input: nums = [34, 23, 1, 24, 75, 33, 54, 8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.

Example 2:
Input: nums = [10, 20, 30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.
'''


def twoSumLessThanK(nums: list[int], target: int) -> int:
    nums.sort()

    ans = -1
    i, j = 0, len(nums) - 1
    while i < j:
        curr_sum = nums[i] + nums[j]
        if curr_sum < target:
            ans = max(ans, curr_sum)
            i += 1
        else:
            j -= 1
        
    return ans