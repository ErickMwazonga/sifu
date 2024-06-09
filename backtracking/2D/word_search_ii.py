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
            if ch not in curr.children:
                return False

            curr = curr.children[ch]

        return curr.is_end


class Solution:

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

        val = board[i][j]
        node = node.children.get(val)

        if not node:
            return

        board[i][j] = '#'  # visit
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            self.dfs(board, node, i + dx, j + dy, path + val, res)

        board[i][j] = val  # unvisit
