'''
88. Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Examples:
Input:
nums1 = [1, 2, 3, 0, 0, 0],  m = 3
nums2 = [2, 5, 6],           n = 3

Output: [1, 2, 2, 3, 5, 6]

Write a function to merge our lists of orders into one sorted list.
my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
'''


def merge_lists(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j = n - 1, m - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    if j >= 0:
        nums1[:k+1] = nums2[:j+1]

    if i >= 0:
        nums1[:k+1] = nums2[:i+1]


def merge_lists_v2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j, k = j - 1, k - 1

    while i >= 0:
        nums1[k] = nums1[i]
        i, k = i - 1, k - 1
