'''
208. Implement Trie (Prefix Tree)
Link: https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve
keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
'''


class TrieNode:

    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                new_node = TrieNode(ch)
                curr.children[ch] = new_node
                curr = new_node

        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False

        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False

        return True
