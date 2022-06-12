'''
796. Rotate String
https://leetcode.com/problems/rotate-string/

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = 'abcde', then it will be 'bcdea' after one shift.

Example 1:
Input: s = 'abcde', goal = 'cdeab'
Output: true

Example 2:
Input: s = 'abcde', goal = 'abced'
Output: false
'''


class Solution:
    def rotateString(s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True

        return False

    def rotateString_v2(s, goal):
        n, m = len(s), len(goal)

        if n > m:
            return False

        if n == 0:
            return True

        return all(s[(n + i) % n] == goal[i] for i in range(m))


class Solution_V2:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        text, pattern = s + s, goal
        n, m = len(text), len(pattern)

        lps = self.build_lps(pattern)

        i, j = 0, 0
        while i < n:
            if text[i] == pattern[j]:
                i, j = i + 1, j + 1

                if j == m:
                    return True
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

        return False

    def build_lps(self, pattern):
        lps = [0] * len(pattern)
        prev_lps, i = 0, 1

        while i < len(pattern):
            if pattern[i] == pattern[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps, i = prev_lps + 1, i + 1
            else:
                if prev_lps == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prev_lps = lps[prev_lps - 1]

        return lps
