'''
LeetCode 152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an
array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4] -> 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1] -> 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution:
    '''Time complexity: ~N, Space complexity: ~1'''
    
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = nums[0]
        min_product = max_product = 1

        for num in nums:
            choices = num, min_product * num, max_product * num
            min_product = min(choices)  
            max_product = max(choices)                      
            res = max(res, max_product)

        return res