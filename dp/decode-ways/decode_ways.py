'''
91. Decode Ways
Link: https://leetcode.com/problems/decode-ways/
Resource: https://inner-game.tistory.com/460

A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Examples:
1. '12' -> 2
    Explanation: It could be decoded as 'AB' (1 2) or 'L' (12).

2. '226' -> 3
    Explanation: It could be decoded as 'BZ' (2 26), 'VF' (22 6), or 'BBF' (2 2 6).
'''


class Solution:
    '''Time: O(2^n), Space: O(n)'''

    def numDecodings(self, s):
        if not s:
            return 0

        return self.dfs(s, i=0)

    def dfs(self, s, i):
        n = len(s)

        if i < n and s[i] == '0':
            return 0

        if i >= n - 1:
            return 1

        ans = self.dfs(s, i + 1)
        if int(s[i: i+2]) <= 26:
            ans += self.dfs(s, i + 2)

        return ans


class Solution_V2:
    '''Time: O(2*n) - O(n), Space: O(n)'''

    def numDecodings(self, s):
        if not s:
            return 0

        memo = {}
        return self.dfs(s, i=0, memo=memo)

    def dfs(self, s, i, memo):
        n = len(s)

        if i < n and s[i] == '0':
            return 0

        if i >= n - 1:
            return 1

        if i in memo:
            return memo[i]

        ans = self.dfs(s, i + 1, memo)
        if int(s[i: i+2]) <= 26:
            ans += self.dfs(s, i + 2, memo)

        memo[i] = ans
        return ans
