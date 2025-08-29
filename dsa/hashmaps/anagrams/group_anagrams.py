'''
49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example:
Input: strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
Output: [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]

More Examples:
1. [''] -> [['']]
2. ['a'] -> [['a']]
'''


from collections import defaultdict


def group_anagrams(strs):
    '''Time O(M.NlogN), Space O(M)'''

    mapping = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))  # tuple(sorted(word))
        mapping[sorted_word] = mapping.get(sorted_word, []) + [word]

    return list(mapping.values())


def group_anagrams_v2(strs):
    '''Time O(M.NlogN), Space O(M)'''

    mapping = defaultdict(list)

    for word in strs:
        sorted_word = tuple(sorted(word)) # key must be immutable, list is not
        mapping[sorted_word].append(word)

    return list(mapping.values())


class Solution_V3:
    '''Time O(MN), Space O(M)'''

    def group_anagrams(self, strs):
        grouping = defaultdict(list)

        for word in strs:
            encoding = self.encode_word(word)
            grouping[tuple(encoding)].append(word)  # list cannot be a key

        return grouping.values()

    def encode_word(self, word):
        '''Establish a 26 letter mapping'''

        mapping = [0] * 26

        for ch in word:
            val = ord(ch) - ord('a')
            mapping[val] += 1

        return mapping
