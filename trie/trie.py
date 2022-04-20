'''
https://www.askpython.com/python/examples/trie-data-structure
'''


class TrieNode:
    '''A node in the trie structure'''

    def __init__(self, char):
        self.char = char  # the character stored in this node
        self.is_end = False  # whether this can be the end of a word
        self.children = {}  # a dictionary of child nodes,  keys are characters, values are nodes

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0


class Trie:

    def __init__(self):
        '''
        The trie has at least the root node.
        The root node does not store any character
        '''
        self.root = TrieNode('')

    def insert(self, word):
        '''Insert a word into the trie'''

        curr_node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                # If a character is not found, create a new curr_node in the trie
                new_curr_node = TrieNode(char)
                curr_node.children[char] = new_curr_node
                curr_node = new_curr_node

        curr_node.is_end = True  # Mark the end of a word
        curr_node.counter += 1  # To indicate that we see this word once more

    def dfs(self, node, pre):
        if node.is_end:
            self.output.append((pre + node.char))

        for child in node.children.values():
            self.dfs(child, pre + node.char)

    def search(self, word):
        curr_node = self.root

        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                # if query doesn't match the nodes in trie
                return []

        self.output = []
        self.dfs(curr_node, word[:-1])

        return self.output


trie = Trie()
trie.insert('Here')
trie.insert('Hear')
trie.insert('Her')
trie.insert('He')
trie.insert('Hello')
trie.insert('How')
trie.insert('xow')
