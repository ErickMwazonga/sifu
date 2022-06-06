'''
28. Implement strStr()
https://leetcode.com/problems/implement-strstr/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = 'hello', needle = 'll'
Output: 2

Example 2:
Input: haystack = 'aaaaa', needle = 'bba'`
Output: -1
'''


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length, needle_length = len(haystack), len(needle)

        if not needle or not haystack:
            return 0

        if haystack == needle:
            return 0

        if needle_length > haystack_length:
            return 0

        # for i in range(haystack_length - n + 1):
        for i in range(haystack_length):
            if haystack[i:i + needle_length] == needle:
                return i

        return -1


class Solution_V2:

    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            return -1

        n, m = len(haystack), len(needle)

        if m > n:
            return -1

        if m == n:
            return 0 if haystack == needle else -1

        lps = self.get_lps(needle)
        i, j = 0, 0

        while i < n:
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

            if j == m:
                return i - m

        return -1
        return -1 if j < m else i-j  # remove the last check

    def get_lps(self, s):
        lps = [0] * len(s)
        prev_lps, i = 0, 1

        while i < len(s):
            if s[i] == s[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps, i = prev_lps + 1, i + 1
            else:
                if prev_lps == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prev_lps = lps[prev_lps - 1]

        return lps
