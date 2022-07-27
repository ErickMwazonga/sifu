# `Reduce()`
Reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an initial argument. <br>
The Python `reduce()` function reduces a list into a single value.

## Syntax
`reduce(func, iterable[, initial])`

## Example 1 - Sum of all numbers
### Without reduce
```py
scores = [79, 65, 64, 75, 66]
total = 0

for score in scores:
    total += score

>>> total # 349
```

### With reduce
```py
from functools import reduce

def sum(a, b):
    print(f'a = {a}, b = {b}, {a} + {b} = {a + b}')
    return a + b


scores = [79, 65, 64, 75, 66]
total = reduce(sum, scores)

>>> total # 349

a = 79, b = 65, 79 + 65 = 144
a = 144, b = 64, 144 + 64 = 208
a = 208, b = 75, 208 + 75 = 283
a = 283, b = 66, 283 + 66 = 349
```

### Using lambda function
```py
from functools import reduce
scores = [79, 65, 64, 75, 66]

total = reduce(lambda a, b: a + b, scores)
>>> total # 349
```

## Example 2 - Min and Max of all numbers
### Using custom function
```py
from functools import reduce

def mini(a, b):
    return a if a < b else b
    # return min(a, b)

def maxi(a, b):
   return a if a > b else b
   # return max(a, b)

nums = [3, 5, 2, 4, 7, 1]

min_val = reduce(mini, nums) # 1
max_val = reduce(maxi, nums) # 7
```

### Using lambda function
```py
from functools import reduce

nums = [3, 5, 2, 4, 7, 1]

min_val =  reduce(lambda a, b: min(a, b), nums) # 1
max_val =  reduce(lambda a, b: max(a, b), nums) # 7
```