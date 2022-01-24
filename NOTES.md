# Table of contents

## Circular Indexing / Iteration
Given an array [1, 2, 3, 4, 5, 6]

To get the next index for circular indexing:

```py
n = len(arr)
index = 0

next_index = (index + 0) % n
```

Another Example
```py
n = len(arr)
index = 3

for i in range(n):
    res.append(A[index])
    index = (index + 1) % n
```
---
## Flatten an Array
### 1. Basic iterative function
```py
def flatten(input):
    new_list = []
    for i in input:
        for j in i:
            new_list.append(j)
    return new_list
```
### 2. Using array functions
```py
def flatten(input):
    new_list = []
    for i in input:
        new_list.extend(i)
    return new_list
```

### 3. Flatten List of Lists Using sum
`sum` has an optional argument: sum(iterable [, start]), so you can do:
```py
regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
flat_list = sum(regular_list, []) # [] + [1, 2, 3, 4] + [5, 6, 7] + [8, 9]

flat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Find i,j in a flattened 2d matrix
Given a 2 matrix, 
```py
[[1, 2, 3],
 [3, 4, 5],
 [6, 7, 8]]
```
that has be flattened to [1, 2, 3, 4, 5, 6, 7, 8, 9].

**Challenge**: 
How do you find the position of an element in the matrix given index i in the flattened list?

```py
# Trick
rows, cols = len(matrix), len(matrix[0])
left, right = 0, rows * cols

item_idx = idx
i, j = idx // cols, idx % cols  # divmod(idx, cols)

# Example - index 7
i, j = divmod(7, cols) # (2, 1) -> i.e row: 2, col: 1

print(matrix[2][1]) # 7
```


