'''
208. Implement Trie (Prefix Tree)
Resources: [
    https://bit.ly/3QdY1qi,
    https://www.youtube.com/watch?v=qA8l8TAMyig,
    https://pythonwife.com/trie-in-python/,
    https://www.lavivienpost.com/autocomplete-with-trie-code/
]
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

    def dfs(self, node, combo, res):
        if node.is_end:
            res.append(combo)

        for child in node.children.values():
            self.dfs(child, combo + child.char, res)

    def get_words(self):
        res, combo = [], ''
        self.dfs(self.root, combo, res)
        return res

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []

            node = node.children[ch]

        res = []
        self.dfs(node, prefix, res)
        return res

    def remove_word(self, node, word, idx=0):
        # end of word but it has other children of other words, we can't remove it
        if len(word) == idx:
            node.is_end = False
            return node.children > 0  # bool(node.children)

        # we need to check if the current node has some children.
        # if it has, the word we want to remove is a prefix of another word. We can not remove it.
        char = word[idx]
        if char not in node.children:
            return True

        next_deletion = self.remove_word(node.children[char], word, idx+1)
        if next_deletion:
            return True

        node.children.pop(char)
        return bool(node.children) or node.is_end

    def longestPrefix(self):
        curr = self.root
        prefix = ''

        while curr:
            if len(curr.children) > 1 or curr.is_end:
                return prefix

            key = list(curr.children)[0]
            prefix += key

            curr = curr.children[key]

        return prefix


trie = Trie()
words = ['Here', 'Hear', 'Her', 'He', 'Herp', 'Hello', 'Heartbeat', 'Hebron']
for word in words:
    trie.insert(word)

assert trie.search('Him') == False
assert trie.search('Hello') == True

assert trie.startsWith('Hel') == True
assert trie.startsWith('Hek') == False

trie_words = [
    'He', 'Her', 'Here',  'Herp', 'Hear', 'Heartbeat', 'Hello', 'Hebron'
]
assert trie.get_words() == trie_words

assert trie.longestPrefix() == 'He'

assert trie.autocomplete('Her') == ['Her', 'Here', 'Herp']
assert trie.autocomplete('Hea') == ['Hear', 'Heartbeat']
