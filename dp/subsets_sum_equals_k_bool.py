'''
Given a set of positive integers and an integer s, 
is there any non-empty subset whose sum to s.
'''


def subset_sum(A, n, sum):
    '''Time: O(2^n), Space: O(n)'''

    # return true if sum becomes 0 (subset found)
    if sum == 0:
        return True

    # base case: no items left or sum becomes negative
    if n < 0 or sum < 0:
        return False

    # Case 1. include current item in the subset (A[n]) and recur
    # for remaining items (n - 1) with remaining sum (sum - A[n])
    include = subset_sum(A, n - 1, sum - A[n])

    # Case 2. exclude current item n from subset and recur for
    # remaining items (n - 1)
    exclude = subset_sum(A, n - 1, sum)

    # return true if we can get subset by including or excluding the
    return include or exclude


def subset_sum_v2(A, n, sum, lookup):
    # return true if sum becomes 0 (subset found)
    if sum == 0:
        return True

    # base case: no items left or sum becomes negative
    if n < 0 or sum < 0:
        return False

    # construct an unique dict key from dynamic elements of the input
    key = (n, sum)

    # if sub-problem is seen for the first time, solve it and
    # store its result in a dict
    if key not in lookup:

        # Case 1. include current item in the subset (A[n]) and recur
        # for remaining items (n - 1) with decreased sum (sum - A[n])
        include = subset_sum_v2(A, n - 1, sum - A[n], lookup)

        # Case 2. exclude current item n from subset and recur for
        # remaining items (n - 1)
        exclude = subset_sum_v2(A, n - 1, sum, lookup)

        # assign true if we get subset by including or excluding current item
        lookup[key] = include or exclude

    return lookup[key]
