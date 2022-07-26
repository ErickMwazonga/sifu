# Declarations

## Single line variable declaration - Mutability
### Immutable data types - integers
```py
>>> a, b, c = 1, 2, 3
>>> print(a, b, c) # 1 2 3

>>> a = b = c = 1 # all three names refer to same int object with value 1
>>> print(a, b, c) # 1 1 1

>>> b = 2 # b now refers to another int object, one with a value of 2
>>> print(a, b, c) # 1 2 1
```

### Mutable data types - integers
```py
>>> x = y = [7, 8, 9] # x and y refer to the same list object -> [7, 8, 9]
>>> x = [13, 8, 9] # x now refers to a different list object -> [13, 8, 9]
>>> print(y) # [7, 8, 9] -> y still refers to the list it was first assigned

# Referring to the same object in memory
>>> x = y = [7, 8, 9] # x and y are two different names for the SAME list object
>>> x[0] = 13 # value of object x is being updated through one of its names

>>> print(x) # [13, 8, 9]
>>> print(y) # [13, 8, 9] -> The change is cascaded because they refer to the same object in memnory
```
