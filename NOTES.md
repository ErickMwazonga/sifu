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

```py
def transpose(strs):
  grid = [list(str) for str in strs]
  return list(map(list, zip(*grid)))

### 1. Basic iterative function
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
---
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
---
## Reverse Iterables
### 1. By `reverse()`
It reverses an iterable in-place
```py
systems = ['Windows', 'macOS', 'Linux']
systems.reverse()
print(systems) # ['Linux', 'macOS', 'Windows']
```

### 2. By Slicing -> `[::-1]`
```py
systems = ['Windows', 'macOS', 'Linux']
reversed_list = systems[::-1]
print(systems) # ['Linux', 'macOS', 'Windows']

# Printing Elements in Reversed Order
n = len(systems)
for i in range(n-1, -1, -1):
    print(systems[i])
```

### 3. By `reversed()`
```py
systems = ['Windows', 'macOS', 'Linux']
reversed_systems = reversed(systems)
print(list(reversed_systems)) # ['Linux', 'macOS', 'Windows']

# Printing Elements in Reversed Order
for system in reversed(systems):
    print(system)
```

## Sort Iterables
### 1. By `sort()`
Sorts an iterable in place

```py
prime = [11, 3, 7, 5, 2]
prime.sort()
print(prime) # [2, 3, 5, 7, 11]
```

### 2. By `sorted()`
```py
prime = [11, 3, 7, 5, 2]
new_prime = sorted(prime)
print(new_prime) # [2, 3, 5, 7, 11]
```

### Syntax: Pameters
`sort()` and `sorted()` hav two optional parameters:<br>
1. `reverse` - If True, the sorted list is descending order<br> 
2. `key` - function that serves as a key for the sort comparison

### Sort the list in Descending order
```py
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print(vowels) # ['u', 'o', 'i', 'e', 'a']
```

### Sort with custom key function
```py
# Sort by lenth of strings in a list
list.sort(key=len)
sorted(list, key=len)

e,g
words = ['pinapples', 'grape', 'apples', 'mangoes']
sorted(words, key=len) # ['grape', 'apples', 'mangoes', 'pinapples']
```

### Sort a list of list by sum
```py
nums = [[7, 9], [2, 4], [8, 1], [5, 6]]
sorted(nums, key=sum) # [[2, 4], [8, 1], [5, 6], [7, 9]]
```

---
### Sort dictionary
```py
sorted_dict = sorted(d.items(), key=lambda x: x[1])
sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
sorted_dict = dict(sorted_dict)

# NB
Sorting by the first index is the default sorting mechanism
>>> nums = [[7, 9], [2, 4], [8, 1], [5, 6]]
>>> sorted_nums = sorted(nums, key=lambda x: x[0])
>>> sorted_list = sorted(nums)

>>> sorted_nums == sorted_list # TRUE

---

# Alternatively
sorted(d, key=d.get, reverse=True):

# Examples
employees = [
    {'Name': 'Sifu', 'age': 25, 'salary': 10000},
    {'Name': 'Chepe', 'age': 30, 'salary': 81000},
    {'Name': 'Ericko', 'age': 18, 'salary': 110000},
]

employees.sort(key=lambda x: x.get('Name'))
employees.sort(key=lambda x: x.get('salary'), reverse=True)
```
---
## Heaps
```py
import heapq
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### minHeap
`heapq.heapify(lst)`
<br/>

### maxHeap
1. Solution: `heapq._heapify_max(lst)`

```py
lst = [5, 1, 3, 7, 2]

heapq._heapify_max(lst)
pop_max = heapq._heappop_max(lst)
```
2. Solution: **Use Negatives**

```py
array = [1, 4, 6, 2, 5, 3, 9, 8, 7]
maxHeap = []
for num in array:
    heapq.heappush(maxHeap, -num)

print("maxHeap:", maxHeap)
# maxHeap: [-9, -8, -6, -7, -2, -3, -4, -1, -5]
```
---
## Traversals
### Depth First Searh
Implemented using a STACK
<br/>
### Breadth First Search
Implemented using a QUEUE

---
## Infinity
-sys.maxsize
-inf, inf


## Algorithms' Summary
Self notes:
- **Brute Force** approach finds all the possible solutions and selects desired solution per given the constraints.
- **Dynamic Programming** also uses Brute Force approach to find the OPTIMUM solution, either maximum or minimum.
- **Backtracking** also uses Brute Force approach but to find ALL the solutions.
  - Solutions to the Backtracking problems can be represented as **State-Space Tree**.
  - The constrained applied to find the solution is called Bounding function.
  - Backtracking follows **Depth-First Search method**.
  - Branch and Bound is also a Brute Force approach, which uses Breadth-First Search method.

## STR TO INT: INT TO STR
### `ord()`
Returns an integer representing the Unicode character for your input string.
```py
>>> [ord(str(i)) for i in range(0, 10)]
# [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

import string
>>> [ord(i) for i in string.ascii_uppercase]
# [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

>>> [ord(i) for i in string.ascii_lowercase]
# [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
```

#### Getting a corresponding integer from an integer character
```py
>>> ch = '5'
>>> ord(ch) - ord('0')
# 5
```

### `chr()`
Returns a character (a string) from an integer (represents unicode code point of the character)

```py
>>> val = 5 
# it's corresponding unicode is 53 = 48 + 5: ord('0') + 5
>>> val_repr = ord('0') + val
>>> char_rep = chr(val_repr)
# 5
```

### Random
`random.randint(a, b)`

Return a random integer N such that a <= N <= b. Alias for `randrange(a, b+1)`