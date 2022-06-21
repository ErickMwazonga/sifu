'''
Given a set of positive integers and an integer s, 
is there any non-empty subset whose sum to s.
'''


def subset_sum(A, n, sum):
    '''Time: O(2^n), Space: O(n)'''

    if sum == 0:
        return True

    if n < 0 or sum < 0:
        return False

    include = subset_sum(A, n - 1, sum - A[n])  # Case 1. include
    exclude = subset_sum(A, n - 1, sum)   # Case 2. exclude

    return include or exclude


def subset_sum_v2(A, n, sum, lookup):
    if sum == 0:
        return True

    if n < 0 or sum < 0:
        return False

    key = (n, sum)
    if key in lookup:
        return lookup[key]

    include = subset_sum_v2(A, n - 1, sum - A[n], lookup)  # Case 1. include
    exclude = subset_sum_v2(A, n - 1, sum, lookup)  # Case 2. exclude

    lookup[key] = include or exclude

    return lookup[key]
