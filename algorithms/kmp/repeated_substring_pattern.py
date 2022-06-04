'''
459. Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/
Resource: https://www.youtube.com/watch?v=lumwBLJOQpk

Given a string s, check if it can be constructed by taking a substring of
it and appending multiple copies of the substring together.

Examples:
1. 'abab' -> True
    Explanation: It is the substring 'ab' twice.
2. 'aba' -> False
3. 'abcabcabcabc' -> True
    Explanation: It is the substring 'abc' four times or the substring 'abcabc' twice.
'''


class Solution_V1:
    '''Time: O(n²), Space: O(n)'''

    def repeatedSubstringPattern(self, s):
        n = len(s)
        half_length = n // 2

        for i in range(1, half_length + 1):
            if s == s[:i] * (n//i):
                return True

        return False


class Solution_V3:
    '''Time: O(n), Space: O(n)'''

    def repeated_substring(self, s):
        n = len(s)
        lps_table = self.get_lps(s)
        lps = lps_table[n-1]

        return lps > 0 and n % (n-lps) == 0

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


class Solution_V3:
    '''Time: O(n), Space: O(n)'''

    def repeated_substring_v3(s):
        return s in (s+s)[1:-1]
