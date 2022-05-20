'''
698. Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
 
Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1, 2, 3, 4], k = 3
Output: false
'''


def canPartitionKSubsets(A, k: int) -> bool:
    n = len(A)
    return backtrack(A, n - 1, k)


def backtrack(A, n, k):
    if k == 0:
        return True

    if n < 0 or k < 0:
        return False

    include = backtrack(A, n - 1, k - A[n])
    exclude = backtrack(A, n - 1, k)

    return include or exclude
