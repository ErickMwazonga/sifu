'''
1752. Check if Array Is Sorted and Rotated
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

Given an array nums, return true if the array was originally sorted in non-decreasing order,
then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Examples:
1. [3, 4, 5, 1, 2] -> True
    Explanation: [1, 2, 3, 4, 5] is the original sorted array.
    You can rotate the array by x = 3 positions to begin on the the element of value 3: [3, 4, 5, 1, 2].

2. [2, 1, 3, 4] - False
    Explanation: There is no sorted array once rotated that can make nums.

3. [1, 2, 3] -> True
    Explanation: [1, 2, 3] is the original sorted array.
    You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
'''
