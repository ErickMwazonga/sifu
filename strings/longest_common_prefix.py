'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"] -> "fl"

Example 2:
Input: strs = ["dog","racecar","car"] -> ""
Explanation: There is no common prefix among the input strings.
'''


def longestCommonPrefix(strs) -> str:
    l = list(zip(*strs))
    prefix = ''

    for i in l:
        if len(set(i)) == 1:
            prefix += i[0]
        else:
            break

    return prefix


def longestCommonPrefix(strs) -> str:
    if not strs or len(strs) == 0:
        return ""

    for i in range(len(strs[0])):
        c = strs[0][i]

        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]

    return strs[0] if strs else ""
