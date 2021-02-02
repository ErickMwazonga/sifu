'''
['X', ' ', ' ', ' ', 'X']
[' ', 'X', ' ', 'X', ' ']
[' ', ' ', 'X', ' ', ' ']
[' ', 'X', ' ', 'X', ' ']
['X', ' ', ' ', ' ', 'X']
'''


def draw_x(N):
    grid = [([' '] * N) for _ in range(N)]

    n, m = N - 1, N - 1
    col, row = 0, 0

    while row <= n and col <= m:
        # First row
        grid[row][col] = 'X'
        grid[row][m] = 'X'

        # Last row
        grid[n][col] = 'X'
        grid[n][m] = 'X'

        m -= 1
        n -= 1
        col += 1
        row += 1

    display_grid(grid)


def display_grid(grid):
    for row in grid:
        print(row)


draw_x(6)
