# Find i, j in a flattened 2d matrix
Given a 2 matrix, 
```py
[[1, 2, 3],
 [3, 4, 5],
 [6, 7, 8]]
```
Flattened to `[1, 2, 3, 4, 5, 6, 7, 8, 9]`

### **Challenge**: <br>
How do you find the position of an element in the matrix given index i in the flattened list?

```py
# Trick
rows, cols = len(matrix), len(matrix[0])
left, right = 0, rows * cols

item_idx = idx
i, j = idx // cols, idx % cols  # divmod(idx, cols)

# Example - index 7
i, j = divmod(7, cols) # (2, 1) -> i.e row: 2, col: 1

>>> matrix[2][1] # 7
```