'''
Find the Minimum Element in a Sorted and Rotated Array
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


def minElementInRotatedSortedArray(arr):
    ''' solve this problem in O(logn) time complexity.'''

    n = len(arr)

    # If the array has only one element, arr = {1}
    if n == 1:
        return arr[0]

    start, end = 0, n - 1

    '''
    If the array is sorted, arr = {1, 2, 3, 4},
    then the minimum element is the element present
    at index 0.
    '''

    if arr[0] < arr[end]:
        return arr[0]

    while (start <= end) {
        mid = start + (end - start) // 2

        if(start < mid && arr[mid] < arr[mid-1]):
            return arr[mid]

        elif(end > mid && arr[mid+1] < arr[mid]):
            return arr[mid+1]

        elif(arr[end] > arr[mid]):
            end = mid-1

        else:
            start = mid + 1

    return -1 