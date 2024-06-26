'''
704. Binary Search
Link: https://leetcode.com/problems/binary-search/

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


def linear_search(data: list[int], target: int) -> bool:
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


def binary_search(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        # mid = low + (high - low) // 2  # To prevent overflow

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def binary_search_v2(arr: list[int], target: int) -> int:
    low, high = 0, len(arr)
    ans = binary_search_helper(arr, low, high, target)
    return ans

def binary_search_helper(arr: list[int], low: int, high: int, x: int) -> int:
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if x == arr[mid]:
        return mid

    if x > arr[mid]:
        return binary_search_helper(arr, mid+1, high, x)
    else:
        return binary_search_helper(arr, low, mid-1, x)
    

assert binary_search_v2([2, 3, 4, 10, 40], 3) == 1
assert binary_search_v2([-1, 0, 3, 5, 9, 12], 9) == 4
