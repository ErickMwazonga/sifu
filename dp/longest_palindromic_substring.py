'''
5. Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/
Resource: https://www.youtube.com/watch?v=IrD8MA054vA

Given a string s, return the longest palindromic substring in s.

Examples:
1. 'babad' -> 'bab' => Note: 'aba' is also a valid answer.
2. 'cbbd' -> 'bb'
3. 'a' -> 'a'
4. 'ac' -> 'a'
'''


class Solution:

    def longestPalindrome(self, s):
        if not s:
            return ''

        n, longest = len(s), ''
        for mid in range(n):
            # odd case, like "aba"
            sub = self.find_palindrome_from(s, mid, mid)
            longest = max(longest, sub)

            # even case, like "abba"
            sub = self.find_palindrome_from(s, mid, mid + 1)
            longest = max(longest, sub)

        return longest

    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break

            left -= 1
            right += 1

        # Because left will go negatively e.g -1
        return string[left + 1: right]


class Solution_V2:
    def longestPalindrome(self, s):
        n, longest = len(s), ''

        for i in range(n):
            # odd cases
            odd_pali = self.get_palindrome(s, i, i)
            longest = max((longest, odd_pali), key=len)

            # even cases
            even_pali = self.get_palindrome(s, i, i+1)
            longest = max((longest, even_pali), key=len)

        return longest

    def get_palindrome(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break

            left -= 1
            right += 1

        return s[left+1:right]
