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

    include = subset_sum(A, n - 1, sum - A[n])
    exclude = subset_sum(A, n - 1, sum)

    return include or exclude


def subset_sum_v2(A, n, sum, memo):
    if sum == 0:
        return True

    if n < 0 or sum < 0:
        return False

    key = (n, sum)
    if key in memo:
        return memo[key]

    include = subset_sum_v2(A, n - 1, sum - A[n], memo)
    exclude = subset_sum_v2(A, n - 1, sum, memo)

    memo[key] = include or exclude
    return memo[key]
