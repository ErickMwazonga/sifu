'''
211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:
Input
['WordDictionary', 'addWord', 'addWord', 'addWord', 'search', 'search', 'search', 'search']
[[], ['bad'], ['dad'], ['mad'], ['pad'], ['bad'], ['.ad'], ['b..']]
Output
[null, null, null, null, false, true, true, true]
'''


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(ch)
            curr = curr.children[ch]

        curr.is_end = True

    def search(self, word: str) -> bool:
        root = self.root
        return self.dfs(root, word, i=0)

    def dfs(self, node, word, i):
        if i == len(word):
            return node.is_end

        if word[i] == '.':
            for child in node.children:
                new_node = node.children[child]
                if self.dfs(new_node, word, i+1):
                    return True
        else:
            if word[i] in node.children:
                new_node = node.children[word[i]]
                return self.dfs(new_node, word, i+1)

        return False
