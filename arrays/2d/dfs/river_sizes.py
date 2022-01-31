'''
You are given a two-dimensional array of potentially unequal height and width. It contains only 0s and 1s.
This array represents a map: 0s are land, and 1s are water. A "river" on this map consists of any number of contiguous,
adjacent water squares, where "adjacent" means "above", "below", "to the left of",
or "to the right of" (that is, diagonal squares are not adjacent).
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


def riverSizes(matrix):
    output = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                river_size = check(i, j, matrix)
                output.append(river_size)

    return output


def check(i, j, matrix):
    outside = i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i])

    if outside or matrix[i][j] == 0:
        return 0

    matrix[i][j] = 0  # SINK

    top = check(i-1, j, matrix)
    down = check(i+1, j, matrix)
    left = check(i, j-1, matrix)
    right = check(i, j+1, matrix)

    return 1 + top + down + left + right


input = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

assert sorted(riverSizes(input)) == [1, 2, 2, 2, 5]
