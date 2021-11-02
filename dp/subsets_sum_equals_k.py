'''
Subsets that sum up to k
Given an array arr of strictly positive integers, and an integer k,
create a function that returns the number of subsets of arr that sum up to k.

Example 1:
    Input: arr = [1, 2, 3, 1], k = 4
    Output: 3
        Explanation: subsets that sum up to k are [1, 2, 1], [1, 3], and [3, 1]
Example 2:
    Input: arr = [1, 2, 3, 1, 4], k = 6
    Output: 4
        Explanation: subsets that sum up to k are [1, 2, 3], [1, 1, 4], [2, 3, 1], and [2, 4]
Example 3:
    Input: arr = [2, 4, 2, 6, 8], k = 7
    Output: 0
        Explanation: there are no subsets that sum up to k
'''


def subsetsThatSumUpToK(arr, k, i=0, _sum=0):
    '''
    Time complexity: O(2^n)
    Space complexity: O(n)
    '''

    if _sum == k:
        return 1
    elif _sum > k or i >= len(arr):
        return 0
    else:
        include = subsetsThatSumUpToK(arr, k, i+1, _sum + arr[i])
        exclude = subsetsThatSumUpToK(arr, k, i+1, _sum)
        return include + exclude


def subsetsThatSumUpToK(arr, k):
    '''
    Time complexity: O(nk)
    Space complexity: O(nk)
    '''

    def rec(arr, k, i, sum, memoiz):
        key = str(i) + " " + str(sum)

        if memoiz.get(key) is not None:
            return memoiz[key]
        elif sum == k:
            return 1
        elif sum > k or i >= len(arr):
            return 0
        else:
            include = subsetsThatSumUpToK(arr, k, i+1, sum + arr[i], memoiz)
            exclude = subsetsThatSumUpToK(arr, k, i+1, sum, memoiz)
            nbSubsets = include + exclude
            memoiz[key] = nbSubsets

        return nbSubsets

    return rec(arr, k, 0, 0, {})
