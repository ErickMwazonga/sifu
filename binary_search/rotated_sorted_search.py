'''
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

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


class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # left part is in order
            if nums[left] <= nums[mid]:
                # target is also in left part
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right part is in order
            else:
                # target is also in right part
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


class Solution2:
    '''https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/894031/Python-O(logn)-Detailed-Explanation'''

    def search(self, nums: list[int], target: int) -> int:
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
