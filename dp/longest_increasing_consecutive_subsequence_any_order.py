'''
128. Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Given an array of integers, find the length of the
longest sub-sequence such that elements in the subsequence are
consecutive integers, the consecutive numbers can be in any order.

Example 1
[1, 9, 3, 10, 4, 20, 2] -> 4
Explanation: The subsequence 1, 3, 4, 2 is the longest subsequence of consecutive elements

Example 1
[36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42] -> 5
Explanation: The subsequence 36, 35, 33, 34, 32 is the longest subsequence of consecutive elements.
'''


def longest_subsequence(A: list) -> int:
    '''Time: O(n), Space: O(n)'''

    visited = set(A)
    max_len = 0

    for num in A:
        count = 1
        forward = num + 1

        while forward in visited:
            count += 1
            forward += 1

        max_len = max(max_len, count)

    return max_len


def longest_subsequence_v2(A: list) -> int:
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


assert longest_subsequence([1, 9, 3, 10, 4, 20, 2]) == 4
assert longest_subsequence([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]) == 5
assert longest_subsequence([-1, 0, 1]) == 3

assert longest_subsequence_v2([1, 9, 3, 10, 4, 20, 2]) == 4
assert longest_subsequence_v2(
    [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]) == 5
assert longest_subsequence([-1, 0, 1]) == 3
