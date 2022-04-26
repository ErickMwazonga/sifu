'''
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ['eat','tea','tan','ate','nat','bat']
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
        sorted_word = ''.join(sorted(word))

        # mapping[sorted_word] = mapping.get(sorted_word, []) + [item]
        if sorted_word not in mapping:
            mapping[sorted_word] = [word]
        else:
            mapping[sorted_word].append(word)

    return list(mapping.values())


def groupAnagrams_v2(strs):
    mapping = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        mapping[sorted_word].append(word)

    return list(mapping.values())


def groupAnagrams_v3(strs):
    '''Time O(m.n) -> Credit: https://programmer.group/leetcode-49-group-anagrams.html'''

    res = defaultdict(list)

    for s in strs:
        count = [0] * 26  # Establish a 26 letter mapping

        for char in s:
            count[ord(char) - ord('a')] += 1  # Freq of each letter

        # Add the array of the corresponding Value, list cannot be a key hence tuple
        res[tuple(count)].append(s)

    return res.values()
