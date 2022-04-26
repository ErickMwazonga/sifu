'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Examples:
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]

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


def topKFrequent_v2(nums, k):
    freqs = {}
    n = len(nums)

    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1

    bucket = [[] for _ in range(n + 1)]
    for key, val in freqs.items():
        bucket[val].append(key)

    res = []
    for i in range(n, -1, -1):
        res.extend(bucket[i])

    return res[:k]


assert topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert topKFrequent([1], 1) == [1]
