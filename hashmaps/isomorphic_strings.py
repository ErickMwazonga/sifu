'''
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/description/

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
'''

def isIsomorphic(s: str, t: str) -> bool:
    if len(set(s)) != len(set(t)):
        return False

    seen = {}
    for ch_s, ch_t in zip(s, t):
        if ch_s not in seen:
            seen[ch_s] = ch_t
        else:
            if seen[ch_s] != ch_t:
                return False
    return True


assert isIsomorphic('egg', 'add') == True
assert isIsomorphic('foo', 'bar') == False
assert isIsomorphic('paper', 'title') == True

