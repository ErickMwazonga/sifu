'''
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Examples:
1. 'A man, a plan, a canal: Panama' -> True
    Explanation: 'amanaplanacanalpanama' is a palindrome.
2 'race a car' -> False
    Explanation: 'raceacar' is not a palindrome.
'''


def isPalindrome(s):
    newS = [i.lower() for i in s if i.isalnum()]
    return newS == newS[::-1]


def isPalindrome_v2(s: str) -> bool:
    s = s.lower()
    res = ''

    for ch in s:
        if ch.isalnum():
            res += ch

    return res == res[::-1]


def isPalindrome_v3(s):
    i, j = 0, len(s) - 1

    while i < j:
        if not s[i].isalnum():
            i += 1
            continue

        if not s[j].isalnum():
            j -= 1
            continue

        if s[i].lower() != s[j].lower():
            return False

        i, j = i + 1, j - 1

    return True
