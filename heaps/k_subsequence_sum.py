'''
2099. Find Subsequence of Length K With the Largest Sum
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

You are given an integer array nums and an integer k. 
You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some
or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [2, 1, 3, 3], k = 2
Output: [3, 3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
Input: nums = [-1, -2, 3, 4], k = 3
Output: [-1, 3, 4]
Explanation:
The subsequence has the largest sum of -1 + 3 + 4 = 6.
'''

import heapq


def maxSubsequence(nums, k: int):
    heap = []

    for i, num in enumerate(nums):
        heapq.heappush(heap, (-num, i))

    res = []
    for _ in range(k):
        num, idx = heapq.heappop(heap)
        # res.append(nums[idx])
        res.insert(0, nums[idx])

    return res
