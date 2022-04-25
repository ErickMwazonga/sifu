'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1, 1, 1, 2, 2, 3],  k = 2
Output: [1, 2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''


import heapq


def top_K_frequent(nums, k):
    freqs = {}
    n = len(nums)

    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1

    bucket = [[] for _ in range(n + 1)]
    for key, val in freqs.items():
        bucket[val].append(key)

    print(bucket)
    res = []
    for i in range(n, -1, -1):
        res.extend(bucket[i])

    return res[:k]


assert top_K_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
# assert top_K_frequent([1], 1) == [1]


def top_K_frequent_XX(nums, k):
    res, freqs = [], {}

    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1

    freqs = [(-v, k) for k, v in freqs.items()]
    heapq.heapify(freqs)

    for _ in range(k):
        v, k = heapq.heappop(freqs)
        res.append(k)

    return res


assert top_K_frequent_XX([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert top_K_frequent_XX([1], 1) == [1]
