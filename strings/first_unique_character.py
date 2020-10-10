'''
Given a string, find the first non-repeating character in it 
and return it's index. If it doesn't exist, return -1.

s = "leetcode" -> return 0.
s = "loveleetcode", -> return 2.
Note: You may assume the string contain only lowercase letters.
'''

def firstUniqChar(s: str):
    '''
    Time complexity : O(N) since we go through the string of length N two times.
    Space complexity : O(N) since we have to keep a hash map with N elements.
    '''
    _hash = {}

    for char in s:
        _hash[char] = _hash.get(char, 0) + 1

    for i in range(len(s)):
        if _hash[s[i]] == 1:
            return i

    return -1
