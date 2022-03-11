'''
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appears
only once and returns the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

Example 1:
[1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of
nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of
nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values
are set beyond the returned length.
'''


def removeDuplicates(nums):
    i = 1

    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1

    return len(nums)


def remove_duplicates(nums):
    n = len(nums)
    count = 1

    for i in range(1, n):
        if nums[i] > nums[i-1]:
            nums[count] = nums[i]
            count += 1

    return count


def removeDuplicates(A):
    count = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            count += 1

    return count


def remove_duplicates(arr):
    seen, res = set(), []

    for num in arr:
        if num not in seen:
            seen.add(num)
            res.append(num)

    return res
