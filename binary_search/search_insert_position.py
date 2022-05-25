'''
35. Search Insert Position - 
Problem - Link: https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1, 3, 5, 6], target = 5
Output: 2

Example 2:
Input: nums = [1, 3, 5, 6], target = 7
Output: 4
'''


def search_insert(nums, target):
    '''Intuition - Just find the lowest than target'''

    low, high = 0, len(nums)

    while low < high:
        mid = low + (high - low) // 2

        if nums[mid] >= target:
            high = mid
        else:
            low = mid + 1

    return low


assert search_insert([1, 3, 5, 6], 5) == 2
assert search_insert([1, 3, 5, 6], 2) == 1
assert search_insert([1, 3, 5, 6], 7) == 4
assert search_insert([1, 3, 5, 5, 6], 0) == 0
assert search_insert([1], 0) == 0
