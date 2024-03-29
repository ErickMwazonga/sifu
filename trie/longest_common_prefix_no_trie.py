'''
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ''.

Examples:
1. ['flower', 'flow', 'flight'] -> 'fl'
2. ['dog', 'racecar', 'car'] -> '' => Explanation: There is no common prefix among the input strings.
'''


def longestCommonPrefix(strs) -> str:
    commonLetters = list(zip(*strs))
    prefix = ''

    for letters in commonLetters:
        if len(set(letters)) == 1:
            prefix += letters[0]
        else:
            break

    return prefix


def longestCommonPrefix_v2(strs) -> str:
    if not strs or len(strs) == 0:
        return ''

    for i in range(len(strs[0])):
        c = strs[0][i]

        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]

    return strs[0] if strs else ''
