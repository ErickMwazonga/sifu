# Flatten an Array

## 1. Using nested loops

```py
def flatten(matrix: list[list]):
    new_list: list[int] = []

    for row in matrix:
        for num in row:
            new_list.append(num)

    return new_list

# Comprehension
result = [item for row in matrix for item in row]
```

## 2. Using a single loop with `extend`

```py
def flatten(matrix: list[list]):
    new_list: list[int] = []

    for row in matrix:
        new_list.extend(row)

    return new_list
```

## 3. Flatten List of Lists using sum

syntax: `result = sum(input_list, [])`

`sum` has an optional argument: `sum(iterable [, start])`, so you can do:

```py
Row = list[int]

nums: list[Row] = [
    [1, 2, 3, 4],
    [5, 6, 7],
    [8, 9]
]

flat_list: list[Row] = sum(nums, []) # [] + [1, 2, 3, 4] + [5, 6, 7] + [8, 9]

>>> flat_list # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

[Why does this work?](https://mathieularose.com/how-not-to-flatten-a-list-of-lists-in-python)

## 4. Using `reduce` function

```py
from functools import reduce
result = list(reduce(lambda a, b: a + b, input_list))
```

## 5. Using `more_itertools` package

```py
import more_itertools
result = list(more_itertools.flatten(input_list))
```

## 6. Using Numpy `cancatenate` function

```py
import numpy as np
result = list(np.concatenate(input_list))
```
