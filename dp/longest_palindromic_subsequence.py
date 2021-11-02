'''
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad" -> "bab"
Note: "aba" is also a valid answer.

Input: s = "cbbd" -> "bb"
Input: s = "a" -> "a"
Input: s = "ac" -> "a"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        longest = ""
        for mid in range(len(s)):
            sub = self.find_palindrome_from(s, mid, mid)
            if len(sub) > len(longest):
                longest = sub

            sub = self.find_palindrome_from(s, mid, mid + 1)
            if len(sub) > len(longest):
                longest = sub

        return longest

    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break

            left += 1
            right -= 1

        # not string[left:right+1] because we are going outside
        return string[left + 1: right]
