'''
208. Implement Trie (Prefix Tree)
Link: https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as 'try') or prefix tree is a tree data structure used to efficiently store and retrieve
keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input
['Trie', 'insert', 'search', 'search', 'startsWith', 'insert', 'search']
[[], ['apple'], ['apple'], ['app'], ['app'], ['app'], ['app']]

Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert('apple');
trie.search('apple');   // return True
trie.search('app');     // return False
trie.startsWith('app'); // return True
trie.insert('app');
trie.search('app');     // return True
'''


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end = False


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

    def search(self, word):
        '''Time: O(m)'''

        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False

            curr = curr.children[ch]

        return curr.is_end

    def startsWith(self, prefix):
        '''Time: O(m)'''

        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False

            curr = curr.children[ch]

        return True
