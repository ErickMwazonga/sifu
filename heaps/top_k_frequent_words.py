'''
692. Top K Frequent Words
Link: https://leetcode.com/problems/top-k-frequent-words/

Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest.
Sort the words with the same frequency by their lexicographical order.

Example 1:
Input: words = ['i','love','leetcode','i','love','coding'], k = 2
Output: ['i', 'love']

Example 2:
Input: words = ['the','day','is','sunny','the','the','the','sunny','is','is'], k = 4
Output: ['the','is','sunny','day']
'''

import heapq


def topKFrequent(words, k):
    res, freqs = [], {}

    for word in words:
        freqs[word] = freqs.get(word, 0) + 1

    freqs = [(-v, k) for k, v in freqs.items()]
    heapq.heapify(freqs)

    for _ in range(k):
        v, k = heapq.heappop(freqs)
        res.append(k)

    return res


words = ['i', 'love', 'leetcode', 'i', 'love', 'coding']
assert topKFrequent(words, 2) == ['i', 'love']

words = ['the', 'day', 'is', 'sunny', 'the', 'the', 'the', 'sunny', 'is', 'is']
assert topKFrequent(words, 4) == ['the', 'is', 'sunny', 'day']
