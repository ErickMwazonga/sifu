'''
https://leetcode.com/problems/valid-sudoku/
Valid Sudoku
Determine if a 9x9 Sudoku board is valid. Only the filled cells
need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the 9 3x3 sub-boxes of the grid must contain the
digits 1-9 without repetition.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        seen = set()

        for row in range(size):
            for col in range(size):
                num = board[row][col]

                if num != ".":
                    col_val = num + "col" + str(col)
                    row_val = num + "row" + str(row)
                    block_val = num + "block" + str(row // 3) + str(col // 3)
                    
                    if col_val in seen or row_val in seen or block_val in seen:
                        return False
                    else:
                        seen.update([row_val, col_val, block_val])
        return True


from typing import List, Union
Unit = List[Union[int, str]]
Matrix = List[Unit]

class SodukuValidator:
    def check_board(self, board: Matrix) -> bool:
        if len(board) != 9:
            return False
        for row in board:
            if len(row) != 9:
                return False
        return True

    def is_unit_valid(self, unit: Unit) -> bool:
        unit = [i for i in unit if i != '.' and i]
        return len(unit) == len(set(unit))

    def check_rows(self, board: Matrix) -> bool:
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def check_cols(self, board: Matrix) -> bool:
        n = len(board)
        for i in range(n):
            column = []
            for j in range(n):
                column.append(board[j][i])

            if not self.is_unit_valid(column):
                return False
        return True

    def check_squares(self, board: Matrix) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s_square = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]

                if not self.is_unit_valid(s_square):
                    return False
        return True

    def isValidSudoku(self, board: Matrix) -> bool:
        if not self.check_board(board):
            return False
        return self.check_rows(board) and self.check_cols(board) and self.check_squares(board)

    # Other nice to have utils
    def transformer(self, grouping: Unit) -> list:
        for i in range(len(grouping)):
            try:
                value = int(grouping[i])
            except ValueError:
                value = 0
            grouping[i] = value
        return grouping

    def check_duplicates(self, grouping: Unit) -> bool:
        grouping = self.transformer(grouping)

        unique_digits = set()
        for num in grouping:
            if num != 0 and num in unique_digits:
                return False
            unique_digits.add(num)
        return True


# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

valid2 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
invalid2= [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

sv = SodukuValidator()
assert sv.isValidSudoku(valid) == True
assert sv.isValidSudoku(invalid) == False
assert sv.isValidSudoku(easy) == True
assert sv.isValidSudoku(hard) == True
assert sv.isValidSudoku(valid2) == True
assert sv.isValidSudoku(invalid2) == False 
