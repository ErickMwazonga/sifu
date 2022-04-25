'''
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order,
find the lowing and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]

Example 2:
Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
'''


def search_range(nums, target):
    n = len(nums)
    result = [-1, -1]

    for i, num in enumerate(nums):
        if num != target:
            continue
        else:
            result[0], result[1] = i, i

            while i+1 < n and nums[i+1] == target:
                result[1] = i
                i += 1

    return result


print(search_range([5, 7, 7, 8, 8, 10], 8))


def first_and_last(A, target):
    n = len(A)

    for i in range(n):
        if A[i] == target:
            start = i

            while i+1 < n and arr[i+1] == target:
                i += 1
            return [start, i]

    return [-1, -1]


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


class Solution:

    def search_range(self, nums, target):
        start = self.find_starting_index(nums, target)
        end = self.find_fnding_index(nums, target)

        return [start, end]

    def find_starting_index(self, nums, target):
        low, high = 0, len(nums)
        index = -1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                index = mid
                high = mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1

        return index

    def find_fnding_index(self, nums, target):
        low, high = 0, len(nums)
        index = -1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1

        return index


soln = Solution()
arr, target = [1, 4, 7, 8, 11, 11, 11, 11, 11, 13], 11
assert soln.search_range(arr, target) == [4, 8]
