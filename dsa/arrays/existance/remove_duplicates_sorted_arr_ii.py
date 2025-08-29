'''
80. Remove Duplicates from Sorted Array II
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example:
Input: nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
Output: 7, nums = [0, 0, 1, 1, 2, 3, 3, _, _]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''


def removeDuplicates(nums: list[int]) -> int:
    n = len(nums)

    if n < 3:
        return n

    idx = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[idx-2]:
            nums[idx] = nums[i]
            idx += 1

    return idx


def removeDuplicates_v2(nums: list[int]) -> int:
    n = len(nums)

    if n < 3:
        return n

    pos = 1
    for i in range(1, n-1):
        if nums[i-1] != nums[i+1]:
            nums[pos] = nums[i]
            pos += 1

    nums[pos] = nums[-1]
    return pos + 1


def removeDuplicates_v3(nums: list[int]) -> int:
    n, pos = len(nums), 2

    for i in range(2, n):
        if nums[pos-2] == nums[pos-1] == nums[i]:
            continue

        nums[pos] = nums[i]
        pos += 1

    return pos
