'''
392. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., 'ace' is a subsequence of 'abcde' while 'aec' is not).

Example 1:
Input: s = 'abc', t = 'ahbgdc'
Output: true

Example 2:
Input: s = 'axc', t = 'ahbgdc'
Output: false
'''


def isSubsequence(s: str, t: str) -> bool:
    sIdx, tIdx = 0, 0

    while sIdx < len(s) and tIdx < len(t):
        if s[sIdx] == t[tIdx]:
            sIdx += 1

        tIdx += 1

    return sIdx == len(s)


assert isSubsequence('abc', 'ahbgdc') == True
assert isSubsequence('axc', 'ahbgdc') == False
