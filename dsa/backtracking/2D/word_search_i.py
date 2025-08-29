'''
79. Word Search
Link: https://leetcode.com/problems/word-search/
Resource: https://www.youtube.com/watch?v=RqffW0smIbQ

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where 'adjacent' cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:
board =
[['A', 'B', 'C', 'E'],
 ['S', 'F', 'C', 'S'],
 ['A', 'D', 'E', 'E']]

Other Examples
1. 'ABCCED' -> true
2. 'SEE' -> true
3. 'ABCB' -> false
'''


class Solution:
    '''Time: O(n * m * 4^n)'''

    def exist(self, board, word) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                if self.dfs(board, row, col, word, 0):
                    return True

        return False

    def dfs(self, board, row, col, word, word_index):
        if word_index == len(word):
            return True

        n, m = len(board), len(board[0])
        out_bounds = row < 0 or row >= n or col < 0 or col >= m
        if out_bounds or word[word_index] != board[row][col] or board[row][col] == '#':
            return False

        val = board[row][col]
        board[row][col] = '#'  # visit node and it's neighbors
        # visited = set()

        # check whether can find 'word' along one direction
        checks = []
        for dx, dy in self.directions:
            check = self.dfs(board, row + dx, col + dy, word, word_index + 1)
            checks.append(check)

        found = any(checks)

        board[row][col] = val  # unvisit
        # visited.remove((row, col))  # reset visited
        return found

    @property
    def directions(self):
        return [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Solution_V2:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not word:
            return False

        n, m = len(board), len(board[0])
        for row in range(n):
            for col in range(m):
                if self.dfs(board, word, 0, row, col):
                    return True

        return False

    def dfs(self, board, word, index, x, y):
        n, m = len(board), len(board[0])
        if index == len(word):
            return True

        if not(0 <= x < n) or not(0 <= y < m) or board[x][y] != word[index]:
            return False

        val = board[x][y]
        board[x][y] = '#'

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            if self.dfs(board, word, index + 1, x + dx, y + dy):
                return True

        board[x][y] = val
        return False
