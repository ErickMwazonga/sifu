'''
516. Longest Palindromic Subsequence
Link: https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by 
deleting some or no elements without changing the order of the remaining elements. 

Examples:
1. 'bbbab' -> 4
2. 'cbbd' -> 2
Explanation: One possible longest palindromic subsequence is 'bb'.
'''


class Solution:
    '''WITHOUT MEMOIZATION'''

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.dfs(s, 0, len(s) - 1)

    def dfs(self, s, start: int, end: int) -> int:
        if start > end:
            return 0

        if start == end:
            return 1

        if s[start] == s[end]:
            return 2 + self.dfs(s, start + 1, end - 1)
        else:
            length_left = self.dfs(s, start + 1, end)
            length_right = self.dfs(s, start, end - 1)

            return max(length_left, length_right)


class Solution_V2:
    '''WITH MEMOIZATION'''

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.dfs(s, 0, len(s) - 1, {})

    def dfs(self, s, start: int, end: int, cache) -> int:
        if start > end:
            return 0

        if start == end:
            return 1

        if (start, end) in cache:
            return cache[(start, end)]

        if s[start] == s[end]:
            cache[(start, end)] = 2 + self.dfs(s, start + 1, end - 1, cache)
        else:
            length_left = self.dfs(s, start + 1, end, cache)
            length_right = self.dfs(s, start, end - 1, cache)
            cache[(start, end)] = max(length_left, length_right)

        return cache[(start, end)]
