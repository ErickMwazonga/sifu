'''
79. Word Search
https://leetcode.com/problems/word-search/
https://www.youtube.com/watch?v=RqffW0smIbQ
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution:
    def exist(self, board, word) -> bool:
        if not board:
            return False

        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if self.dfs(board, i, j, word, []):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word, visited) -> bool:
        if len(word) == 0:  # all the characters are checked
            return True

        # boundary check + isVisisted + cannot be self
        n, m = len(board), len(board[0])
        if (i < 0 or i >= n or j < 0 or j >= m
            or word[0] != board[i][j] or (i, j) in visited
            ):
            return False

        visited.append((i, j))

        # check whether can find "word" along one direction
        up = self.dfs(board, i+1, j, word[1:], visited)
        down = self.dfs(board, i-1, j, word[1:], visited)
        left = self.dfs(board, i, j+1, word[1:], visited)
        right = self.dfs(board, i, j-1, word[1:], visited)

        nxt = up or down or left or right

        if not nxt:
            visited.pop()  # avoid visit agian

        return nxt
