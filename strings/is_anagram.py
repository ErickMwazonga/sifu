'''
242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Examples
1. Input: s = 'anagram', t = 'nagaram'
Output: true

2. Input: s = 'rat', t = 'car'
Output: false
You may assume the string contains only lowercase alphabets.
'''

from collections import Counter


def is_anagram(s1: str, s2: str) -> bool:
    '''
    INTUITION: Compare counts of each char in both strings
    Time O(N^2), Space O(1)
    '''
    
    if len(s1) != len(s2):
        return False

    for ch in set(s1):
        if s1.count(ch) != s2.count(ch):
            return False

    return True


def is_anagram_v2(s1: str, s2: str) -> bool:
    '''
    INTUITION: Sorting
    Time O(NlogN), Space O(1)
    '''

    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


def is_anagram_v2(s1: str, s2: str) -> bool:
    '''
    INTUITION: Compare frequencies
    Time O(NlogN), Space O(1)
    '''

    if len(s1) != len(s2):
        return False

    _freqs, _freq2 = {}, {}

    for ch in s1:
        _freqs[ch] = _freqs.get(ch, 0) + 1

    for ch in s2:
        _freq2[ch] = _freq2.get(ch, 0) + 1

    for ch in _freqs:
        if ch not in _freq2 or _freqs[ch] != _freq2[ch]:
            return False

    return True


def is_anagram_v3(s1: str, s2: str) -> bool:
    '''
    INTUITION: Reduce frequency on encounters
    Time O(NlogN), Space O(1)
    '''
    
    if len(s1) != len(s2):
        return False

    char_count = dict(Counter(s1)) # same as freqs.get(ch, 0) for all elems
    
    for ch in s2:
        if ch not in char_count or char_count[ch] == 0:
            return False
        char_count[ch] -= 1
    
    return True



assert is_anagram('anagram', 'nagaram') == True
assert is_anagram('rat', 'car') == False
