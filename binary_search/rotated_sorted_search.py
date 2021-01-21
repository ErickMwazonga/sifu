'''
33. Search in Rotated Sorted Array
You are given an integer array nums sorted in ascending order, and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7]
might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''

from typing import List

class Solution:
    '''https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/894031/Python-O(logn)-Detailed-Explanation'''

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid

            # inflection point to the right. Left is strictly increasing
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # inflection point to the left of me. Right is strictly increasing
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1