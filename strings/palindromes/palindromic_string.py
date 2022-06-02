'''
2108. Find First Palindromic String in the Array
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

Given an array of strings words, return the first palindromic string in the array.
If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.

Examples:
1. ['abc', 'car', 'ada', 'racecar', 'cool'] -> 'ada'
2. ['notapalindrome', 'racecar'] -> 'racecar'
3. ['def', 'ghi'] -> ''
'''


def firstPalindrome(words):
    for word in words:
        if word == word[::-1]:
            return word

    return ''
