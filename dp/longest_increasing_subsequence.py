'''
Given an array of integers, find the length of the
longest sub-sequence such that elements in the subsequence are
consecutive integers, the consecutive numbers can be in any order.

Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
Output: 4
Explanation:
The subsequence 1, 3, 4, 2 is the longest
subsequence of consecutive elements

Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
Output: 5
Explanation:
The subsequence 36, 35, 33, 34, 32 is the longest
subsequence of consecutive elements.
'''

from typing import List


def longest_subsequence(A: List) -> int:
    visited = set(A)
    max_len = 0

    for num in nums:
        count = 1
        forward = num + 1

        while forward in visited:
            count += 1
            forward += 1
        max_len = max(max_len, count)

    return max_len

assert longest_subsequence([1, 9, 3, 10, 4, 20, 2]) == 4
assert longest_subsequence([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]) == 5
assert longest_subsequence([-1, 0, 1]) == 3


def longest_subsequence2(A: List) -> int:
    visited = set(A)
    max_len = 0

    for num in A:
        count = 1
        backward, forward = num - 1, num + 1

        while backward in visited:
            count += 1
            backward -= 1
        while forward in visited:
            visited.remove(forward)
            count += 1
            forward += 1
        max_len = max(max_len, count)

    return max_len

assert longest_subsequence2([1, 9, 3, 10, 4, 20, 2]) == 4
assert longest_subsequence2([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]) == 5
assert longest_subsequence([-1, 0, 1]) == 3
