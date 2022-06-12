'''
720. Longest Word in Dictionary
https://leetcode.com/problems/longest-word-in-dictionary/

Given an array of strings words representing an English Dictionary,
return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Examples:
1. ['w','wo','wor','worl','world'] -> 'world'
Explanation: The word 'world' can be built one character at a time by 'w', 'wo', 'wor', and 'worl'.

2. ['a','banana','app','appl','ap','apply','apple'] -> 'apple'
Explanation: Both 'apply' and 'apple' can be built from other words in the dictionary. However, 'apple' is lexicographically smaller than 'apply'.
'''


def longestWord(words: list[str]) -> str:
    words.sort()
    seen, longest = set(), ''

    seen.add('')  # last version of one char is empty string

    for word in words:
        last_version = word[:-1]

        if last_version not in seen:
            continue

        longest = max((longest, word), key=len)
        seen.add(word)

    return longest
