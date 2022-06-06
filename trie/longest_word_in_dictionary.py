'''
720. Longest Word in Dictionary
https://leetcode.com/problems/longest-word-in-dictionary/

Given an array of strings words representing an English Dictionary,
return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Examples:
1. ['w','wo','wor','worl','world'] -> 'world'
Explanation: The word 'world' can be built one character at a time by 'w', 'wo', 'wor', and 'worl'.

2. ['a','banana','app','appl','ap','apply','apple'] -> 'apple'
Explanation: Both 'apply' and 'apple' can be built from other words in the dictionary. 
However, 'apple' is lexicographically smaller than 'apply'.
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.is_end = True


class Solution:
    # DRAW EXAMPLE TO FIND ANSWER
    def longestWord(self, words: list[str]) -> str:
        # sort by combination(len, lexicographically(word))
        words = sorted(words, key=lambda word: (-len(word), word))

        trie = Trie()
        for word in words:
            trie.insert(word)

        for word in words:
            flag = True
            cur = trie.root

            for letter in word:
                if not cur.children[letter].is_end:
                    flag = False
                    break
                else:
                    cur = cur.children[letter]

            if flag:
                return word

        return ''
