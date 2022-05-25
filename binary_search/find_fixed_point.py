'''
Link: https://leetcode.com/problems/fixed-point/
Credit: https://xingxingpark.com/Leetcode-1064-Fixed-Point/

A fixed point in an array 'A' is an index 'i' such that A[i] is equal to 'i'.
Given an array of n distinct integers sorted in ascending order, write a
function that returns a 'fixed point' in the array. If there is not a
fixed point return 'None'

Examples
1. [-10, -5, 0, 3, 7] -> 3 # Fixed point is 3:
2. [0, 2, 5, 8, 17] -> 0 # Fixed point is 0:
3. [-10, -5, 3, 4, 7, 9] -> None # No fixed point. Return 'None'
'''


def find_fixed_point_linear(A):
    '''Time: O(n), Space: O(1)'''

    for i in range(len(A)):
        if A[i] == i:
            return A[i]

    return None


def find_fixed_point(A):
    '''Time: O(log n), Space: O(1)'''

    low, high = 0, len(A) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if A[mid] == mid:
            return A[mid]
        elif A[mid] > mid:
            high = mid - 1
        else:
            low = mid + 1

    return None


assert find_fixed_point([-10, -5, 0, 3, 7]) == 3
assert find_fixed_point([0, 2, 5, 8, 17]) == 3
assert find_fixed_point([-10, -5, 3, 4, 7, 9]) == 3
