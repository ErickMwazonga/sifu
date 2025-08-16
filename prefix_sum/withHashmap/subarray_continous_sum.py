'''
523. Continuous Subarray Sum
Link: https://leetcode.com/problems/continuous-subarray-sum/

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where:
    - its length is at least two, and
    - the sum of the elements of the subarray is a multiple of k.
Note that:
    - A subarray is a contiguous part of the array.
    - An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 
Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false
'''

def checkSubarraySum(nums: list[int], k: int) -> bool:
    mod_map = {0: -1}  # mod value -> earliest index
    prefix_sum = 0
    
    for i, num in enumerate(nums):
        prefix_sum += num
        mod = prefix_sum % k if k != 0 else prefix_sum  # avoid divide by zero
        
        if mod in mod_map:
            if i - mod_map[mod] >= 2:
                return True
        else:
            mod_map[mod] = i
    
    return False