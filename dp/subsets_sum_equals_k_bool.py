'''
Given a set of positive integers and an integer s, is there any non-empty subset whose sum to s.
'''


def subsetSum(A, n, sum):
    '''
    Time complexity: O(2^n)
    Space complexity: O(n)
    '''

    # return true if sum becomes 0 (subset found)
    if sum == 0:
        return True

    # base case: no items left or sum becomes negative
    if n < 0 or sum < 0:
        return False

    # Case 1. include current item in the subset (A[n]) and recur
    # for remaining items (n - 1) with remaining sum (sum - A[n])
    include = subsetSum(A, n - 1, sum - A[n])

    # Case 2. exclude current item n from subset and recur for
    # remaining items (n - 1)
    exclude = subsetSum(A, n - 1, sum)

    # return true if we can get subset by including or excluding the
    # current item
    return include or exclude


# Return true if there exists a subsequence of A[0..n] with given sum
def subsetSumImproved(A, n, sum, lookup):
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
        include = subsetSum(A, n - 1, sum - A[n], lookup)

        # Case 2. exclude current item n from subset and recur for
        # remaining items (n - 1)
        exclude = subsetSum(A, n - 1, sum, lookup)

        # assign true if we get subset by including or excluding current item
        lookup[key] = include or exclude

    # return solution to current sub-problem
    return lookup[key]
