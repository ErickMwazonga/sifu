'''
214. Shortest Palindrome
https://leetcode.com/problems/shortest-palindrome/
Resource: https://www.youtube.com/watch?v=c4akpqTwE5g&t=531s

You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.

Examples:
1. 'aacecaaa' -> 'aaacecaaa'
2. 'abcd' -> 'dcbabcd'
'''


class Solution:

    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        pattern = s + '#' + rev_s  # to prevent lps overlapp

        lps = self.build_lps(pattern)
        k = lps[-1]

        return rev_s + s[k:]
        # return rev_s[:-k] + s

    def build_lps(self, s):
        lps = [0] * len(s)  # first lps val will always be one
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
