'''
1143. Longest Common Subsequence
Link: https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with
some characters(can be none) deleted without changing the relative order of the remaining characters.
(eg, 'ace' is a subsequence of 'abcde' while 'aec' is not).
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
    Input: text1 = 'abcde', text2 = 'ace'  -> 3  
    Explanation: The longest common subsequence is 'ace' and its length is 3.
Example 2:
    Input: text1 = 'abc', text2 = 'abc' -> 3
    Explanation: The longest common subsequence is 'abc' and its length is 3.
'''


class Solution:
    '''
    Time: O(MN). We're solving M * Nsubproblems. Solving each subproblem is an O(1)operation.
    Space: O(MN). We're allocating a 2D array of size M * N to save the answers to subproblems
    '''

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        dp = [[0] * (m+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[n][m]
