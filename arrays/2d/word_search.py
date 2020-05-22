'''
https://leetcode.com/problems/word-search/
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

from typing import List

# REVISIT
def word_search(board: List[List[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(i)):
            if board[i][j] == word[0] and dfs(board, i, j, 0, word):
                return True
    return False


def dfs(board: List[List[str]], i: int, j: int, count: int, word: str) -> bool:
    if count == len(word):
        return True

    if i < 0 or i >= len(board) or j < 0 or j >= len(board) or board[i][j] != word[count]:
        return False

    temp = word[i][j]

