'''
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Determine if a 9x9 Sudoku board is valid. Only the filled cells
need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the 9 3x3 sub-boxes of the grid must contain the
digits 1-9 without repetition.
'''


from collections import defaultdict


def isValidSudoku(board) -> bool:
    seen = set()

    for row in range(9):
        for col in range(9):
            num = board[row][col]

            if num != '.':
                # col_val = num + 'col' + str(col) # f'col-{col}-{num}'
                # row_val = num + 'row' + str(row) # f'row-{row}-{num}'
                # block_val = num + 'block' + str(row // 3) + str(col // 3) # f'block-{row//3}-{col//3}-{num}'

                col_val = f'col-{col}-{num}'
                row_val = f'row-{row}-{num}'
                block_val = f'block-{row//3}-{col//3}-{num}'

                if (col_val in seen) or (row_val in seen) or (block_val in seen):
                    return False
                else:
                    # seen.add(row_val)
                    # seen.add(col_val)
                    # seen.add(block_val)
                    seen.update([row_val, col_val, block_val])

    return True


def isValidSudoku2(board) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for row in range(9):
        for col in range(9):
            val = board[row][col]

            if val == '.':
                continue

            block_val = (row // 3, col // 3)

            if (val in rows[row]) or (val in cols[col]) or (val in squares[block_val]):
                return False

            rows[row].add(val)
            cols[col].add(val)
            squares[block_val].add(val)

    return True
