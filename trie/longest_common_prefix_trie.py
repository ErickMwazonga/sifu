'''
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ''.

Examples:
1. ['flower', 'flow', 'flight'] -> 'fl'
2. ['dog', 'racecar', 'car'] -> '' => Explanation: There is no common prefix among the input strings.
'''


class TrieNode:

    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(ch)

            curr = curr.children[ch]

        curr.is_end = True

    def longestPrefix(self):
        curr = self.root
        prefix = ''

        while len(curr.children) == 1 and not curr.is_end:
            key = list(curr.children.keys())[0]  # list(root.children)[0]
            prefix += key

            curr = curr.children[key]

        return prefix

    def longestPrefix_v2(self):
        curr = self.root
        prefix = ''

        while curr:
            if len(curr.children) > 1 or curr.is_end:
                return prefix

            key = list(curr.children)[0]
            prefix += key

            curr = curr.children[key]

        return prefix


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''

        trie = Trie()

        for word in strs:
            trie.insert(word)

        return trie.longestPrefix()
