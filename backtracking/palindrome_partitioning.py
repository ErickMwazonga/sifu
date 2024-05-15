'''
131. Palindrome Partitioning
Link: https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Examples:
1. 'aab' ->  [['a', 'a', 'b'], ['aa', 'b']]
2. 'a' -> [['a']]
'''


class Solution:
    def partition(self, s: str):
        res = []
        self.backtrack(s, res, start=0, partition=[])
        return res

    def backtrack(self, s, res, start, partition):
        if start == len(s):
            res.append(partition[:])
            return

        for i in range(start, len(s)):
            if not self.is_palindrome(s, start, i):
                return

            partition.append(s[start:i+1])
            self.backtrack(s, res, i + 1, partition)
            partition.pop()

    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False

            i, j = i + 1, j - 1

        return True


class Solution_V2():
    def partition(self, s):
        res = []
        self.dfs(s, res, partition=[])
        return res

    def dfs(self, s, partition, res):
        if not s:
            res.append(partition)

        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], partition+[s[:i]], res)

    def isPalindrome(self, s):
        return s == s[::-1]
