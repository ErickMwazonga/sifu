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

def findMin(self, nums: List[int]) -> int:
    first, last = 0, len(nums) - 1
    
    while first < last:
        midpoint = (first + last) // 2
        
        if nums[midpoint] > nums[last]:
            first = midpoint + 1
        else:
            last = midpoint
            
    return nums[first]


def findMin(self, nums: List[int]) -> int:
    if not nums:
        return -1

    low, high = 0, len(nums) - 1
    mid = low + (high - low) // 2

    while low < high:
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

        mid = low + (high - low) // 2

    return nums[mid]