'''
852. Peak Index in a Mountain Array
Link: https://leetcode.com/problems/peak-index-in-a-mountain-array

You are given an integer mountain array arr of length n where the values 
increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

Examples:
1. [0, 1, 0] -> 1
2. [0, 2, 1, 0] -> 1
3. [0, 10, 5, 2] -> 1
'''

def peakIndexInMountainArray(arr: list[int]) -> int:
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        prev = arr[mid - 1] if mid - 1 >= 0 else float('-inf')
        nxt = arr[mid + 1] if mid + 1 < len(arr) else float('-inf')

        if prev < arr[mid] > nxt:
            return mid
        elif prev < arr[mid] < nxt:
            low = mid
        elif prev > arr[mid] > nxt:
            high = mid

    return low
