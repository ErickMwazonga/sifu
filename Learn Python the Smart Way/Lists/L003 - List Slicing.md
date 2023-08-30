## List Slicing

### Basic Example

```py
>>> A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
>>> A[2:8]
# ['c', 'd', 'e', 'f', 'g', 'h']
```

### Slice with Negative indices

```py
# Note: Last index is -1
​
>>> A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
>>> A[-7:-2]
# ['c', 'd', 'e', 'f', 'g']
```

### Slice with Positive & Negative Indices

```py
>>> A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
>>> A[2:-5]
# ['c', 'd']
```

### Step of the Slicing

```py
# Return every 2nd item between position 2 to 7

>>> A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
>>> A[2:7:2]
# ['c', 'e', 'g']
```

### Negative Step Size

```py
# Return every 2nd item between position 6 to 1

>>> A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
>>> A[6:1:-2]

# ['g', 'e', 'c']
```

### Slice at Beginning & End

```py
# Slice the first three items from the list

>>> A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
>>> A[:3]

# ['a', 'b', 'c']
```

​

# Slice the last three items from the list

```py
>>> A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
>>> A[6:]

# ['g', 'h', 'i']
```

### Reverse a List

```py
>>> A = ['a', 'b', 'c', 'd', 'e']
>>> A[::-1]

# ['e', 'd', 'c', 'b', 'a']
```

### Modify Multiple List Values

```py
### Modify multiple list items

>>> A = ['a', 'b', 'c', 'd', 'e']
>>> A[1:4] = [1, 2, 3]
>>> print(A)

# ['a', 1, 2, 3, 'e']
```

### Replace multiple elements in place of a single element

```py
>>> A = ['a', 'b', 'c', 'd', 'e']
>>> A[1:2] = [1, 2, 3]
>>> print(A)

# ['a', 1, 2, 3, 'c', 'd', 'e']
```

### Delete Multiple List Items

```py
>>> A = ['a', 'b', 'c', 'd', 'e']
>>> A[1:5] = []
>>> print(A)
# ['a']

>>> A = ['a', 'b', 'c', 'd', 'e']
>>> del A[1:5]
>>> print(A)
# ['a']
```

### Clone or Copy a List

```py
>>> A1 = ['a', 'b', 'c', 'd', 'e']
>>> A2 = A1[:]
>>> print(A2)
# ['a', 'b', 'c', 'd', 'e']

>>> print(A2 is A1)
# False
```
