'''
Given a string, find the first non-repeating character in it 
and return it's index. If it doesn't exist, return -1.

Examples
1. 'leetcode' -> 0
2. 'loveleetcode' -> 2
Note: You may assume the string contain only lowercase letters.
'''


def firstUniqChar(s: str):
    '''Time: O(N), Space: O(N)'''

    _hash = {}

    for char in s:
        _hash[char] = _hash.get(char, 0) + 1

    for i in range(len(s)):
        if _hash[s[i]] == 1:
            return i

    return -1


assert firstUniqChar('leetcode') == 0
assert firstUniqChar('loveleetcode') == 2
