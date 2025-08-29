'''
767. Reorganize String
Link: https://leetcode.com/problems/reorganize-string/
Resource: https://www.youtube.com/watch?v=2g_b1aYTHeg

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return '' if not possible.

Examples:
1. 'aab' -> 'aba'
2. 'aaab' -> ''
'''

import heapq


def reorganize_string(s):
    freqs = {}
    for ch in s:
        freqs[ch] = freqs.get(ch, 0) + 1

    max_heap = [(-v, k) for k, v in freqs.items()]
    heapq.heapify(max_heap)

    res = ''
    prev_count, prev_char = 0, ''

    while max_heap:
        curr_count, curr_char = heapq.heappop(max_heap)
        res += curr_char

        if prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_char))

        prev_count, prev_char = curr_count + 1, curr_char

    return res if len(res) == len(s) else ''


def reorganize_string_v2(s: str) -> str:
    freqs = {}
    for ch in s:
        freqs[ch] = freqs.get(ch, 0) + 1

    heap = [(-v, k) for k, v in freqs.items()]
    heapq.heapify(heap)

    res = ''
    prev_count, prev_char = heapq.heappop(heap)
    res += prev_char

    while heap:
        curr_count, curr_char = heapq.heappop(heap)
        res += curr_char

        prev_count += 1
        if prev_count < 0:
            heapq.heappush(heap, (prev_count, prev_char))

        prev_count, prev_char = curr_count, curr_char

    return '' if len(res) != len(s) else res
