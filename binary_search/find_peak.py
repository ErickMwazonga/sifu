'''
162. Find Peak Element
Link: https://leetcode.com/problems/find-peak-element/

Given a non-empty array of integers arr, create a function that returns the index of a peak element.
We consider an element as peak if it's greater than or equal to its neighbors,
the next and previous element (assume that arr[-1] and arr[n] are equal to -∞).
And if there are multiple peaks in arr, just return the index of one of them.

1. [4, 5, 8, 3] -> 2
    Explanation: arr[2] is a peak element because it's greater than or equal to arr[1], 
    and greater than or equal to arr[3]
2. [1, 5, 2, 6, 6, 3] -> 3
    Explanation: arr[3] is a peak element because it's greater than or equal
    to arr[2] and greater than or equal to arr[4] (other valid outputs would be 1 and 4,
    because arr[1] and arr[4] are also peak elements)
'''


def find_peak_v0(nums):
    max_num = max(nums)
    return nums.index(max_num)


def find_peak(arr):
    '''Time: O(n), Space: O(1)'''

    n = len(arr)

    if n < 2:
        return 0

    for i in range(n):
        if i == 0 and arr[i] > arr[i+1]:
            return i

        if i == n-1 and arr[i] > arr[i-1]:
            return i

        if (arr[i] > arr[i-1]) and (arr[i] > arr[i+1]):
            return i

    return -1


def find_peak_v2(nums):
    left, right = 0, len(nums)-1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid

        if nums[mid+1] > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left


def findPeakElement_v3(sf, nums):
    n = len(nums)

    if n == 1:
        return 0

    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        # if we access out of bounds, set to negative infinity
        left_val = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
        right_val = nums[mid + 1] if mid + 1 < n else float('-inf')

        if nums[mid] > right_val and nums[mid] > left_val:
            return mid

        if right_val > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return None


def find_peak_v4(A):
    left, right = 0, len(A) - 1

    while left < right:
        mid = (left + right) // 2

        if A[mid] < A[mid+1]:
            left = mid + 1
        else:
            right = mid

    return left
