'''
410. Split Array Largest Sum

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [7, 2, 5, 10, 8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7, 2, 5] and [10, 8], where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1, 2, 3, 4, 5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1, 2, 3] and [4, 5], where the largest sum among the two subarrays is only 9.
'''

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            mid = (l + r) // 2
            
            if self.canSplit(nums, k, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res

    def canSplit(self, nums: List[int], k: int, largest: int) -> bool:
        subarray_count, cur_sum = 1, 0
        
        for n in nums:
            cur_sum += n

            if cur_sum > largest:
                subarray_count += 1
                cur_sum = n
                
                if subarray_count > k:
                    return False
                
        return True
