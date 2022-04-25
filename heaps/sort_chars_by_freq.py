'''
451. Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/

Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Examples:
1. 'tree' -> 'eert'
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore 'eetr' is also a valid answer.

2. 'cccaaa' -> 'aaaccc'
3. 'Aabb' -> 'bbAa'
'''

import heapq


def frequencySort(s: str) -> str:
    '''Time: O(nlogk), Space: O(n)'''

    res, freqs = '', {}

    for c in s:
        freqs[c] = freqs.get(c, 0) + 1

    freqs = [(-v, k) for k, v in freqs.items()]
    heapq.heapify(freqs)

    while freqs:
        v, k = heapq.heappop(freqs)
        res += k * abs(v)

    return res


def frequencySort_v2(s: str) -> str:
    dic = {}
    result = ''

    for char in s:
        dic[char] = dic.get(char, 0) + 1

    # sort the dic on values in reverse order
    sorted_dic = sorted(dic, key=dic.get, reverse=True)

    for count in sorted_dic:
        result += count * (dic[count])

    return result
