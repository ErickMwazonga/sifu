'''
686. Repeated String Match
https://leetcode.com/problems/repeated-string-match/

Given two strings a and b, return the minimum number of times you should repeat string 'a' so that string 'b' is a substring of it.
If it is impossible for b to be a substring of a after repeating it, return -1.
Notice: string 'abc' repeated 0 times is '', repeated 1 time is 'abc' and repeated 2 times is 'abcabc'.

Example 1:
Input: a = 'abcd', b = 'cdabcdab'
Output: 3
Explanation: We return 3 because by repeating a three times 'abcdabcdabcd', b is a substring of it.

Example 2:
Input: a = 'a', b = 'aa'
Output: 2
'''


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        n, m = len(A), len(B)
        times = (n - 1) // m + 1  # Ceiling.

        for i in range(0, 2):
            index = self.search(A * (times + i), B)

            if index is not None:
                return times + i

        return -1

    def search(self, text, pattern):
        lps = self.build_lps(pattern)
        i, j = 0, 0

        while i < len(text):
            if text[i] == pattern[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

            if j == len(pattern):
                return i - len(pattern)

        return None

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
