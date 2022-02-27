'''
https://leetcode.com/problems/fixed-point/
Credit: https://xingxingpark.com/Leetcode-1064-Fixed-Point/

A fixed point in an array 'A' is an index 'i' such that A[i] is equal to 'i'.
Given an array of n distinct integers sorted in ascending order, write a
function that returns a 'fixed point' in the array. If there is not a
fixed point return 'None'.
'''

# Fixed point is 3:
A = [-10, -5, 0, 3, 7]
# Fixed point is 0:

# A = [0, 2, 5, 8, 17]

# No fixed point. Return 'None':
# A = [-10, -5, 3, 4, 7, 9]


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
        elif A[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1

    return None


print(find_fixed_point(A))
