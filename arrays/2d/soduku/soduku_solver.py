'''
37. Sudoku Solver
https://leetcode.com/problems/sudoku-solver/
Credit: https://aakashjhawar.medium.com/sudoku-solver-using-opencv-and-dl-part-2-bbe0e6ac87c5

Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:

The '.' character indicates empty cells.
'''


class Solution:

    def solve_sudoku(self, board):
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

    def find_next_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.find_next_empty()

        # no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True

        possible_values = [str(x) for x in range(1, 10)]
        for num in possible_values:
            if self.is_safe(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = '.'

        return False

    def is_safe(self, row, col, val):
        safe_row = self.check_row(row, val)
        safe_col = self.check_col(col, val)
        safe_square = self.check_square(row, col, val)

        return safe_row and safe_col and safe_square

    def check_row(self, row, val):
        for col in range(9):
            if self.board[row][col] == val:
                return False
        return True

    def check_col(self, col, val):
        for row in range(9):
            if self.board[row][col] == val:
                return False
        return True

    def check_square(self, row, col, val):
        box_row, box_col = row // 3, col // 3
        box_row_start, box_col_start = box_row * 3, box_col * 3

        for r in range(box_row_start, box_row_start + 3):
            for c in range(box_col_start, box_col_start + 3):
                if self.board[r][c] == val:
                    return False

        return True
