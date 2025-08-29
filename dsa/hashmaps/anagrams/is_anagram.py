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

    for ch in set(s1):
        if s1.count(ch) != s2.count(ch):
            return False

    return True


def is_anagram_v2(s1: str, s2: str) -> bool:
    '''
    INTUITION: Sorting
    Time O(NlogN), Space O(1)
    '''

    return sorted(s1) == sorted(s2)


def is_anagram_v2(s1: str, s2: str) -> bool:
    '''
    INTUITION: Compare frequencies
    Time O(N), Space O(26) # there can only be 26 distinct chars in the freqs
    '''

    freqs, freq2 = {}, {}

    for ch in s1:
        freqs[ch] = freqs.get(ch, 0) + 1

    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1

    # return freqs == freq2
    for ch in freqs:
        if ch not in freq2 or freqs[ch] != freq2[ch]:
            return False

    return True

def is_anagram_v3(s1: str, s2: str) -> bool:
    '''
    INTUITION: Compare frequencies improved
    Time O(N), Space O(26) # there can only be 26 distinct chars in the freqs
    '''

    return Counter(s1) == Counter(s2)

def is_anagram_v4(s1: str, s2: str) -> bool:
    '''
    INTUITION: Reduce frequency on encounters
    Time O(N), Space O(26)
    '''
    
    if len(s1) != len(s2):
        return False

    char_count = dict(Counter(s1)) # same as freqs.get(ch, 0) for all elems
    
    for ch in s2:
        if ch not in char_count or char_count[ch] == 0:
            return False
        char_count[ch] -= 1
    
    return True

class IsAngramV5:
    '''
    INTUITION: Angrams will have the same encoding of 26 letter frequencies
    Time O(N), Space O(26)
    '''

    def is_anagram(self, s1, s2):
        return self.encode_word(s1) == self.encode_word(s2)

    def encode_word(self, word: str) -> tuple:
        encoding = [0] * 26
        for ch in word:
            ch_occurence = ord(ch) - ord('a')
            encoding[ch_occurence] += 1
        return tuple(encoding)



assert is_anagram('anagram', 'nagaram') == True
assert is_anagram('rat', 'car') == False
