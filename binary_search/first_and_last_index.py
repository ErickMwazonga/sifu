'''
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order,
find the lowing and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


def find_first_and_last(A, target):
    # Naive Approach -> O(n)
    n = len(A)
    first, last = -1, -1

    for i in range(n):
        if target != A[i]:
            continue

        if first != -1:
            continue
        else:
            first = i

        last = i

    return [first, last]


class Solution(object):

    def searchRange(self, nums, target):
        start = self.findStartingIndex(nums, target)
        end = self.findEndingIndex(nums, target)

        return [start, end]

    def findStartingIndex(self, nums, target):
        low, high = 0, len(nums) - 1
        index = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    def findEndingIndex(self, nums, target):
        low, high = 0, len(nums) - 1
        index = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index


soln = Solution()
arr, target = [1, 4, 7, 8, 11, 11, 11, 11, 11, 13], 11
assert soln.searchRange(arr, target) == [4, 8]
