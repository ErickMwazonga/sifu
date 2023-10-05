'''
794. Valid Tic-Tac-Toe State
https://leetcode.com/problems/valid-tic-tac-toe-state/description/

Given a Tic-Tac-Toe board as a string array board, return true if and only if it
is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:
Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.


Examples:
1. ["O  ","   ","   "] -> false
    Explanation: The first player always plays "X".

2. ["XOX"," X ","   "] -> false
    Explanation: Players take turns making moves.

3. ["XOX","O O","XOX"] -> true
'''

from functools import reduce


class Solution:

    def __init__(self):
        self.board = None
        self.X_PLAYER = 'X'
        self.O_PLAYER = 'O'

    def validTicTacToe(self, board: list[str]) -> bool:
        self.board = board

        if self.board_is_empty():
            return True

        if any([
            not self.x_has_started(),
            self.has_unmatching_turns(),
            self.has_improper_winning_state()
        ]):
            return False

        return True

    def get_all_board_values(self) -> str:
        return reduce(lambda x, y: x.strip() + y.strip(), self.board, '')

    def x_has_started(self) -> bool:
        all_values = self.get_all_board_values()
        return all_values.count(self.X_PLAYER) >= all_values.count(self.O_PLAYER)

    def x_plays_next(self) -> None:
        pass

    def board_is_empty(self) -> bool:
        touched_rows = filter(
            lambda row: self.X_PLAYER in row or self.O_PLAYER in row, self.board
        )
        return not list(touched_rows)

    def has_unmatching_turns(self) -> bool:
        all_values = self.get_all_board_values()
        x_turns = all_values.count(self.X_PLAYER)
        o_turns = all_values.count(self.O_PLAYER)

        diff_in_turns = x_turns - o_turns
        return diff_in_turns < 0 or diff_in_turns > 1

    def has_improper_winning_state(self) -> bool:
        x_has_won = self.player_has_won(self.X_PLAYER)
        o_has_won = self.player_has_won(self.O_PLAYER)

        return x_has_won and o_has_won

    def section_has_all_similar_values(self, section: list[str], val: str) -> bool:
        return section[0] == val and len(set(section)) == 1

    def player_has_won(self, player: str) -> bool:
        # check rows
        for row in self.board:
            if self.section_has_all_similar_values(row, player):
                return True

        # check cols
        cols = list(zip(*self.board))
        for col in cols:
            if self.section_has_all_similar_values(col, player):
                return True

        # check diagonals
        first_diagonal = [self.board[i][i] for i in range(3)]
        sec_diagonal = [self.board[i][2 - i] for i in range(3)]

        if self.section_has_all_similar_values(first_diagonal, player):
            return True

        if self.section_has_all_similar_values(sec_diagonal, player):
            return True

        return False
