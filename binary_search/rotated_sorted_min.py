'''
153 Find the Minimum Element in a Sorted and Rotated Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Given an array which is sorted in ascending order is
rotated at some unknown point.
Write a code to find the minimum element in a sorted and rotated array.

You may assume no duplicate exists in the array.
Examples
Input: [6, 7, 8, 1, 2] -> 1
Input: [8, 9, 10, 1, 0, 1, 2] -> 0
'''


def naive_approach(A):
    _min = A[0]

    for i in range(1, len(A)):
        if _min > A[i]:
            _min = A[i]

    return _min


def findMin(self, A: list[int]) -> int:
    left, right = 0, len(A) - 1

    while left < right:
        mid = (left + right) // 2

        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid

    return A[left]


def findMin(self, A: list[int]) -> int:
    '''O(logn)'''

    left, right = 0, len(A) - 1

    if A[right] > A[left]:
        return A[left]

    while left < right:
        mid = (left + right) // 2

        if A[mid + 1] < A[mid]:
            return A[mid+1]
        elif A[mid] < A[mid-1]:
            return A[mid]
        elif A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid

    return A[left]
