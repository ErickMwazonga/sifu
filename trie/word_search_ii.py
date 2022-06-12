'''
212. Word Search II
Link: https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.
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
            if ch not in curr.children:
                curr.children[ch] = TrieNode(ch)
            curr = curr.children[ch]

        curr.is_end = True


class Solution:
    def findWords(self, board, words):
        'Time: O(m * n * 4^(m*n)), Space: O(m*n + k)'

        trie = TrieNode()
        root = trie.root

        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        res = set()

        for r in range(rows):
            for c in range(cols):
                # if board[i][j] in set(list(zip(*words))[0]): # Check if letter is a first character
                self.dfs(board, root, r, c, word='', res=res)

        return res

    def dfs(self, board, node, r, c, word, res):
        if node.is_end:
            res.add(word)

        out_of_bounds = r < 0 or c < 0 or r >= len(board) or c >= len(board[0])
        if out_of_bounds or board[r][c] not in node.children or board[r][c] == '#':
            return

        val = board[r][c]
        board[r][c] = '#'

        node = node.children[val]

        self.dfs(board, node, r + 1, c, word + val, res)
        self.dfs(board, node, r - 1, c, word + val, res)
        self.dfs(board, node, r, c - 1, word + val, res)
        self.dfs(board, node, r, c + 1, word + val, res)

        board[r][c] = val


class Solution_V2:

    def findWords(self, board, words):
        trie = Trie()
        node = trie.root

        for word in words:
            trie.insert(word)

        n, m = len(board), len(board[0])
        res = []
        for i in range(n):
            for j in range(m):
                self.dfs(board, node, i, j, '', res)

        return res

    def dfs(self, board, node, i, j, path, res):
        if node.is_end:
            res.append(path)
            node.is_end = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        tmp = board[i][j]
        node = node.children.get(tmp)

        if not node:
            return

        board[i][j] = '#'
        self.dfs(board, node, i+1, j, path + tmp, res)
        self.dfs(board, node, i-1, j, path + tmp, res)
        self.dfs(board, node, i, j-1, path + tmp, res)
        self.dfs(board, node, i, j+1, path + tmp, res)

        board[i][j] = tmp
