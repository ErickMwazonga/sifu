'''
704. Binary Search
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4  -> Index 4

Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1 -> Doesn't exist
'''


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


def binary_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2  # To prevent overflow

        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_v2(arr, low, high, x):
    if low <= high:
        mid = low + (high - low) // 2

        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return binary_search_v2(arr, mid+1, high, x)
        else:
            return binary_search_v2(arr, low, mid-1, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = 10
low, high = 0, len(arr) - 1

print(binary_search_v2(arr, low, high, x))
