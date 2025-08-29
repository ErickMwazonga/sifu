'''
Given an unsorted non-empty array, return the k th smallest element in linear time O(n).

You may modify the array.
You may assume no duplicate values in the value - that is - all values are distinct.
You may assume k is valid such that 1 <= k <= n, where n is the length of array.
You may assume array is non-empty.

The first input is an array and second input is k.

kSmallest([11, 2, 7 10, 5, 4], 2) = 4
Explanation: k= 2. 4 is the 2nd smallest element in the array.
'''

import random


def kthSmallest(arr, n, k):
    arr.sort()
    return arr[k-1]


'''
Method 4 (QuickSelect)
This is an optimization over method 1 if QuickSort is used as a sorting algorithm in first step.
In QuickSort, we pick a pivot element, then move the pivot element to its correct position and 
partition the array around it. The idea is, not to do complete quicksort, but stop at the 
point where pivot itself is k’th smallest element. Also, not to recur for both left and 
right sides of pivot, but recur for one of them according to the position of pivot.
The worst case time complexity of this method is O(n2), but it works in O(n) on average.
'''


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(A, lo, hi):
    pivot = A[lo]
    i = lo + 1
    j = hi

    while True:
        while A[i] < pivot:
            i += 1
            if i == hi:
                break
        while A[j] > pivot:
            j -= 1
            if j == lo:
                break

        if j <= i:
            break
        swap(A, i, j)

    swap(A, lo, j)
    return j


def k_smallest(A, k):
    lo, hi = 0, len(A) - 1
    k = k - 1

    random.shuffle(A)

    while hi > lo:
        j = partition(A, lo, hi)

        if j == k:
            return A[k]
        elif j > k:
            hi = j - 1
        else:
            lo = j + 1

    return A[k]
