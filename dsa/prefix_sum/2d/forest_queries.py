'''
Forest Queries
https://cses.fi/problemset/task/1652

You are given an n times n grid representing the map of a forest. Each square is either empty or contains a tree. The upper-left square has coordinates (1,1), and the lower-right square has coordinates (n,n).
Your task is to process q queries of the form: how many trees are inside a given rectangle in the forest?

Input
The first input line has two integers n and q: the size of the forest and the number of queries.
Then, there are n lines describing the forest. Each line has n characters: . is an empty square and * is a tree.
Finally, there are q lines describing the queries. Each line has four integers y_1, x_1, y_2, x_2 corresponding to the corners of a rectangle.

Output
Print the number of trees inside each rectangle.
4 3
forest = [
  ['.', '*', '.', '.'],
  ['*', '*', '.', '.'],
  ['.', '.', '*', '.'],
  ['.', '.', '*', '*']
]

queries = [
  [2, 2, 3, 4],
  [3, 1, 3, 1],
  [1, 1, 4, 4]
]

Output: [3, 1, 2]
'''

def count_trees_in_queries(
    n: int, forest: list[list[str]], queries: list[list[int]]
) -> list[int]:
    # Create prefix sum matrix with 1-based indexing
    prefix = [[0] * (n + 1) for _ in range(n + 1)]

    # Compute prefix sums
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            tree = 1 if forest[y - 1][x - 1] == '*' else 0
            prefix[y][x] = (
                prefix[y - 1][x] +
                prefix[y][x - 1] -
                prefix[y - 1][x - 1] +
                tree
            )

    # Process queries
    results = []
    for y1, x1, y2, x2 in queries:
        res = (
            prefix[y2][x2]
            - prefix[y1 - 1][x2]
            - prefix[y2][x1 - 1]
            + prefix[y1 - 1][x1 - 1]
        )
        results.append(res)

    return results