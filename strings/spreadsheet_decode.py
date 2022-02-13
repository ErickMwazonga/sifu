'''
168. Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/
Implement a function that converts an integer to the spreadsheet
column ID.

Examples:
1. 1 -> A
2. 27 -> AA
3. 702 -> ZZ
'''


def spreadsheet_decode_column(col_num):
    '''Decodes a column number into a column id.'''

    col_str = ''

    while col_num > 0:
        col_num, remainder = divmod(col_num - 1, 26)
        curr_str = chr(ord('A') + remainder)
        col_str = curr_str + col_str

    return col_str


assert spreadsheet_decode_column(1) == 'A'
assert spreadsheet_decode_column(27) == 'AA'
assert spreadsheet_decode_column(702) == 'ZZ'
