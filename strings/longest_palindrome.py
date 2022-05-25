'''
409. Longest Palindrome
Link: https://leetcode.com/problems/longest-palindrome/

Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, 'Aa' is not considered a palindrome here.

Examples:
1. 'abccccdd' ->  7
One longest palindrome that can be built is 'dccaccd', whose length is 7.

2. 'a' -> 1
3. 'bb' -> 2
'''

from collections import Counter


def longestPalindrome(s: str) -> int:
    freq = Counter(s)

    length = 0
    for _, v in freq.items():
        length += v if v % 2 == 0 else v - 1

    if length < len(s):
        length += 1

    return length
