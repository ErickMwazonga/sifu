'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Examples:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
'''

import heapq


def topKFrequent(nums, k):
    res, freqs = [], {}

    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1

    freqs = [(-v, k) for k, v in freqs.items()]
    heapq.heapify(freqs)

    for _ in range(k):
        v, k = heapq.heappop(freqs)
        res.append(k)

    return res


assert topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert topKFrequent([1], 1) == [1]
