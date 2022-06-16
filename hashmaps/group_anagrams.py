'''
49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
Output: [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]

More Examples:
1. [''] -> [['']]
2. ['a'] -> [['a']]
'''


from collections import defaultdict


def groupAnagrams(strs):
    '''Time O(m.nlogn)'''

    mapping = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))  # tuple(sorted(word))

        # mapping[sorted_word] = mapping.get(sorted_word, []) + [item]
        if sorted_word not in mapping:
            mapping[sorted_word] = [word]
        else:
            mapping[sorted_word].append(word)

    return list(mapping.values())


def groupAnagrams_v2(strs):
    mapping = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))  # tuple(sorted(word))
        mapping[sorted_word].append(word)

    return list(mapping.values())


class Solution_V3:
    '''Time O(m.n) -> Resource: https://programmer.group/leetcode-49-group-anagrams.html'''

    def groupAnagrams(self, strs):
        grouping = defaultdict(list)

        for _str in strs:
            mapping = self.get_mapping(_str)
            grouping[tuple(mapping)].append(_str)  # list cannot be a key

        return grouping.values()

    def get_mapping(self, _str):
        '''Establish a 26 letter mapping'''

        mapping = [0] * 26

        for ch in _str:
            val = ord(ch) - ord('a')
            mapping[val] += 1

        return mapping
