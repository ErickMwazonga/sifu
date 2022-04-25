'''
79. Word Search
https://leetcode.com/problems/word-search/
Credit: https://www.youtube.com/watch?v=RqffW0smIbQ

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
        outside = row < 0 or row >= n or col < 0 or col >= m
        if outside or word[word_index] != board[row][col]:
            return False

        if board[row][col] == '#':
            return False

        # visit node and it's neighbors
        val = board[row][col]
        board[row][col] = '#'

        # check whether can find 'word' along one direction
        up = self.dfs(board, row+1, col, word, word_index+1)
        down = self.dfs(board, row-1, col, word, word_index+1)
        left = self.dfs(board, row, col+1, word, word_index+1)
        right = self.dfs(board, row, col-1, word, word_index+1)

        found = up or down or left or right

        board[row][col] = val
        return found


class Solution2:
    '''Time: O(n * m * 4^n)'''

    def exist(self, board, word) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if self.dfs(board, row, col, word, 0, visited):
                    return True

        return False

    def dfs(self, board, row, col, word, word_index, visited):
        if word_index == len(word):
            return True

        n, m = len(board), len(board[0])
        outside = row < 0 or row >= n or col < 0 or col >= m
        if outside or word[word_index] != board[row][col]:
            return False

        if (row, col) in visited:
            return False

        # visit node and it's neighbors
        visited.add((row, col))
        up = self.dfs(board, row+1, col, word, word_index+1, visited)
        down = self.dfs(board, row-1, col, word, word_index+1, visited)
        left = self.dfs(board, row, col+1, word, word_index+1, visited)
        right = self.dfs(board, row, col-1, word, word_index+1, visited)

        found = up or down or left or right

        visited.remove((row, col))  # reset visited
        return found


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

soln = Solution()
assert soln.exist(board, 'ABCCED') == True
assert soln.exist(board, 'SEE') == True
assert soln.exist(board, 'ABCB') == False
