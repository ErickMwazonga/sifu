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

for in in range(n):
    res.append(A[index])
    index = (index + 1) % n;