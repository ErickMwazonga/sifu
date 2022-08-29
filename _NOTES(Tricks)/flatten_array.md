# Flatten an Array

## 1. Basic iterative function
```py
def flatten(matrix: list[list]):
    new_list: list[int] = []

    for row in matrix:
        for num in row:
            new_list.append(num)

    return new_list
```

## 2. Using array functions
```py
def flatten(matrix: list[list]):
    new_list: list[int] = []

    for row in matrix:
        new_list.extend(row)

    return new_list
```
## 3. Flatten List of Lists using sum
`sum` has an optional argument: `sum(iterable [, start])`, so you can do:
```py
Row = list[int]

regular_list: list[Row] = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
flat_list: list[Row] = sum(regular_list, []) # [] + [1, 2, 3, 4] + [5, 6, 7] + [8, 9]

>>> flat_list # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```