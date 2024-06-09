'''
Resource: https://www.youtube.com/watch?v=b0AgeE6alds

You are given a two-dimensional array of potentially unequal height and width. It contains only 0s and 1s.
This array represents a map: 0s are land, and 1s are water.
A 'river' on this map consists of any number of contiguous,
adjacent water squares, where 'adjacent' means 'above', 'below', 'to the left of',
or 'to the right of' (that is, diagonal squares are not adjacent).
Write a function which returns an array of the sizes of all rivers represented in the input matrix.
Note that these sizes do not need to be in any particular order.

For example:
input = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
];

riverSizes(input); // returns [1, 2, 2, 2, 5]
That is, in this input, there is one river of size 1,
there are three rivers of size 2, and there is one river of size 5.
Hint: it is acceptable to mutate the input arrays.
'''


class Solution:
    def river_sizes(self, matrix):
        output = []

        n, m = len(matrix), len(matrix[i])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    river_size = self.check(matrix, i, j)
                    output.append(river_size)

        return output

    def check(self, matrix, i, j):
        if not self.in_bounds(matrix, i, j) or matrix[i][j] == 0:
            return 0

        matrix[i][j] = 0  # SINK/VISIT
        size = 1

        for dx, dy in self.directions:
            size += self.check(matrix, i + dx, j + dy)

        return size

    @property
    def directions(self):
        return [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def in_bounds(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return (0 <= x < n) and (0 <= y < m)
