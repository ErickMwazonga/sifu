# Circular Indexing / Iteration
Given an array `[1, 2, 3, 4, 5, 6]` <br>
To get the next index for circular indexing:

```py
n: int = len(arr)
index: int = 0

next_index: int = (index + 0) % n
```

### Another Example
```py
n: int = len(arr)
index: int = 3

for i in range(n):
    res.append(A[index])
    index = (index + 1) % n
```

### Practival Example - Check is one array is a rotation of the other
```py
'''
INTUITION
Normal element index = i
Rotated element index = (i + k) % n
    where: n - no of elements, k - offset
'''


def is_rotation(A: list[int], B: list[int]) -> bool:
    n, m = len(A), len(B)

    if n != m:
        return False

    offset: int = -1
    first_num: int = A[0]

    for i, num in enumerate(B):
        if first_num == num:
            offset = i
            break

    if offset == -1:
        return False

    for i in range(n):
        key = (i + offset) % n
        if A[i] != B[key]:
            return False

    return True

A: int = [1, 2, 3, 4, 5, 6, 7]
B: int = [4, 5, 6, 7, 1, 2, 3]

assert is_rotation(A, B) == True
```