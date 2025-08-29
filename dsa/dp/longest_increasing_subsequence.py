'''
300. Longest Increasing Subsequence
Link: https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
[10, 9, 2, 5, 3, 7, 101, 18] -> 4 
Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
'''


def lengthOfLIS(nums):
    '''Time: ~N^2, Space: ~N'''

    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(0, n):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
