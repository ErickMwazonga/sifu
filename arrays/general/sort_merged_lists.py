'''
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

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


def merge_sorted_lists(arr1, arr2):
    '''Time O(nlogn)'''

    return sorted(arr1 + arr2)


def merge_lists(my_list, alices_list):
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    their_index, my_index, merged_index = 0, 0, 0

    while merged_index < merged_list_size:
        if my_index >= len(my_list):
            # Case: my list is exhausted
            merged_list[merged_index] = alices_list[their_index]
            their_index += 1
        elif their_index >= len(alices_list):
            # Case: Their list is exhausted
            merged_list[merged_index] = my_list[my_index]
            my_index += 1
        elif my_list[my_index] < alices_list[their_index]:
            # Case: my item is next
            merged_list[merged_index] = my_list[my_index]
            my_index += 1
        else:
            # Case: Their item is next
            merged_list[merged_index] = alices_list[their_index]
            their_index += 1

        merged_index += 1

    return merged_list


def merge_lists_v2(nums1, n, nums2, m) -> None:
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
