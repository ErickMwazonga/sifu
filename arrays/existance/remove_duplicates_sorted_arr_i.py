'''
26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appears
only once and returns the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

Examples:
1. [1, 1, 2] -> 2 => (length of 2), nums = [1, 2]
2. [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] -> 5 => nums = [0, 1, 2, 3, 4]
'''


def removeDuplicates(nums: list[int]) -> int:
    i = 1

    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1

    return len(nums)


def removeDuplicates_v2(nums: list[int]) -> int:
    count, n = 1, len(nums)

    for i in range(1, n):
        if nums[i] > nums[i-1]:
            nums[count] = nums[i]
            count += 1

    return count


def removeDuplicates_v3(nums: list[int]) -> int:
    seen, res = set(), []

    for num in nums:
        if num not in seen:
            seen.add(num)
            res.append(num)

    return len(res)
