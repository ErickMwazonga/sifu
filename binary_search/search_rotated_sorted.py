'''
33. Search in Rotated Sorted Array
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

You are given an integer array nums sorted in ascending order, and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0, 1, 2, 4, 5, 6, 7]
might become [4, 5, 6, 7, 0, 1, 2]).

If target is found in the array return its index, otherwise, return -1.

Example 1:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4

Example 2:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
'''


class Solution:
    '''[INTUITION]: https://www.youtube.com/watch?v=4Ik1nCLjwcI&list=PLKYEe2WisBTH7I9sCPjSZCs-iBAH4ybmS&index=6'''

    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1

        # get the pivot
        min_idx = self.find_min_index(nums)

        if min_idx == 0: # not rotated
            low, high = 0, n - 1
        elif nums[0] <= target <= nums[min_idx - 1]: # focus search to the left
            low, high = 0, min_idx - 1
        else: # focus search to the right
            low, high = min_idx, n - 1

        return self.binary_search(nums, low, high, target)

    def binary_search(self, nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def find_min_index(self, nums):
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return low
