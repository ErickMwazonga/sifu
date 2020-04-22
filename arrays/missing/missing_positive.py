'''
41. First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.
Example 1:

Input: [1,2,0]
Output: 3

Input: [3,4,-1,1]
Output: 2

Input: [7,8,9,11,12]
Output: 1

Your algorithm should run in O(n) time and uses constant extra space.


the additional space depends on your implementation.
But the time complexity is O(n), because membership check in a set is O(1)
and the for loop complexity is O(n) (same for array to set()).
therefore the overall asymptotic time complexity is O(n).
'''

def first_missing_postive(arr):
    arr = set(arr)
    
    for i in range(1, len(arr)+2):
        if i not in arr:
            return i