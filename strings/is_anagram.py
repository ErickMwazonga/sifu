'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
Given two strings s and t , write a function to determine if t is an anagram of s.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
You may assume the string contains only lowercase alphabets.
'''

def is_anagram_(s1, s2):
    # Requires n log n time (since any comparison 
    s1 = "fairy tales"
    s2 = "rail safety"

    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
        
    _freqs = {}
    
    for c in s1:
        _freqs[c] = _freqs.get(c, 0) + 1
        
    for c in s2:
        if c not in _freqs:
            return False
        else:
            _freqs[c] -= 1
    
    if any(_freqs.values()):
        return False
    # for v in _freqs.values():
    #     if v != 0:
    #         return False
    
    return True

print(is_anagram(s1, s2))