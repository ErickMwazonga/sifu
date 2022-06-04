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
        # link = self.get_lps(B)
        link = [-1] * (len(B) + 1)

        for j in range(len(B) - 1):
            i = j
            while i != -1 and B[j + 1] != B[link[i] + 1]:
                i = link[i]
            link[j + 1] = link[i] + 1

        b_index = -1
        for i in range(-1, len(A) + len(B)):
            if b_index == len(B) - 1:
                return i // len(A) + 1

            while A[(i + 1) % len(A)] != B[b_index + 1] and b_index != -1:
                b_index = link[b_index]

            if A[(i + 1) % len(A)] == B[b_index + 1]:
                b_index += 1
                continue
        return -1

    def get_lps(self, s):
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
