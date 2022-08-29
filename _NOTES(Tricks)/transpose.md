# Transpose 2D array

## 1. Using Normal Loop
```py
def transpose(matrix):
    n, m = len(matrix), len(matrix[0])
    transposed = [[0] * n for _ in range(m)]
    # transposed = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]

    return transposed
```


## 2. Using `zip()`
```py
def transpose(nums: list[int]) :
    grid: list[int] = [list(num) for num in nums]
    return list(map(list, zip(*grid)))
```