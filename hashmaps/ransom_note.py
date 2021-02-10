'''
383. Ransom Note
https://leetcode.com/problems/ransom-note/

Given an arbitrary ransom note string and another string containing letters from
all the magazines, write a function that will return true if the ransom note
can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False

    freqs = {}
    for ch in magazine:
        freqs[ch] = freqs.get(ch, 0) + 1

    for c in ransomNote:
        if c not in freqs or freqs[c] == 0:
            return False

        freqs[c] -= 1

    return True
