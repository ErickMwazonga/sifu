'''
37. Sudoku Solver
Link: https://leetcode.com/problems/sudoku-solver/
Resource: https://aakashjhawar.medium.com/sudoku-solver-using-opencv-and-dl-part-2-bbe0e6ac87c5

Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:

The '.' character indicates empty cells.
'''


class Solution:

    def solveSudoku(self, board):
        self.board = board
        self.solve()

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print('- - - - - - - - - - - - - ')

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(' | ', end='')

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + ' ', end='')

    def solve(self):
        row, col = self.find_next_empty()

        # no unassigned position is found, puzzle solved
        if not row and not col:
            return True

        possible_guesses = [str(x) for x in range(1, 10)]
        for guess in possible_guesses:
            if self.is_safe(row, col, guess):
                self.board[row][col] = guess

                if self.solve():  # continue solving else reset to empty
                    return True

                # if solution not valid or our guess did not solve the soduku
                # then we need to backtrack and try another number
                self.board[row][col] = '.'  # reset the guess

        return False

    def find_next_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col

        return None, None

    def is_safe(self, row, col, guess):
        safe_row = self.check_row(row, guess)
        safe_col = self.check_col(col, guess)
        safe_square = self.check_square(row, col, guess)

        return safe_row and safe_col and safe_square

    def check_row(self, row, guess):
        # return not any(self.board[row][col] == guess for col in range(9))
        for col in range(9):
            if self.board[row][col] == guess:
                return False
        return True

    def check_col(self, col, guess):
        # return all(self.board[row][col] != guess for row in range(9))
        for row in range(9):
            if self.board[row][col] == guess:
                return False
        return True

    def check_square(self, row, col, guess):
        box_row, box_col = row // 3, col // 3
        box_row_start, box_col_start = box_row * 3, box_col * 3

        for r in range(box_row_start, box_row_start + 3):
            for c in range(box_col_start, box_col_start + 3):
                if self.board[r][c] == guess:
                    return False

        return True
