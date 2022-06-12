'''
211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
    word may contain dots '.' where dots can be matched with any letter.

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
        return self.dfs(root, word, idx=0)

    def dfs(self, node, word, idx):
        if not node:
            return False

        if idx == len(word):
            return node.is_end

        char = word[idx]
        if char != '.':
            return self.dfs(node.children.get(char), word, idx + 1)
        else:
            for child in node.children:
                if self.dfs(node.children[child], word, idx + 1):
                    return True

        return False

    def dfs_v2(self, node, word, idx):
        if idx == len(word):
            return node.is_end

        if idx > len(word):
            return False

        val = word[idx]
        if (val != '.') and (val not in node.children):
            return False

        if val != '.':
            self.dfs(node.children.get(val), word, idx + 1)
        else:
            for child in node.children:
                self.dfs(node.children[child], word, idx + 1)

        return True
