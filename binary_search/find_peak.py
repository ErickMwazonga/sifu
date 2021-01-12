'''
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/

Given a non-empty array of integers arr, create a function that returns the index of a peak element.
We consider an element as peak if it's greater than or equal to its neighbors,
the next and previous element (assume that arr[-1] and arr[n] are equal to -∞).
And if there are multiple peaks in arr, just return the index of one of them.

Input: arr = [4, 5, 8, 3] -> 2
    Explanation: arr[2] is a peak element because it's greater than or equal to arr[1], and greater than or equal to arr[3]
Input: arr = [1, 3, 4, 7, 8] -> 4
    Explanation: arr[4] is a peak element because it's greater than or equal to arr[3], which is it's only neighbor
Input: arr = [1, 5, 2, 6, 6, 3] -> 3
    Explanation: arr[3] is a peak element because it's greater than or equal
    to arr[2] and greater than or equal to arr[4] (other valid outputs would be 1 and 4, because arr[1] and arr[4] are also peak elements)
'''

def findPeak(arr):
    '''Time: O(n), Space: O(1)'''
    n = len(arr)
    
    for i in range(n):
        if (
            (i == 0 or arr[i] >= arr[i-1]) and
            (i == n-1 or arr[i] >= arr[i+1])
        ):
            return i

# ITERATIVELY
def findPeak(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid

    return left

# RECURSIVELY
def findPeakRec(arr, left, right):
    if left >= right:
        return left
        
    mid = (left + right) // 2

    if arr[mid] < arr[mid+1]:
        return findPeakRec(arr, mid+1, right)
    else:
        return findPeakRec(arr, left, mid)

def findPeak(arr):
    return findPeakRec(arr, 0, len(arr)-1)