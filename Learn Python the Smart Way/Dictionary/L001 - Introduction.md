# Dictionary

Dictionaries are Python’s implementation of a data structure, generally known as associative arrays, hashes, or hashmaps.
It is a mapping between a set of indexes (known as keys) and a set of values. Each key maps to a value.

### Properties of a Dictionary

1. Keys must be unique:
   A key can appear in a dictionary only once.
2. Key must be immutable type:
   You can use any object of immutable type as dictionary keys – such as numbers, strings, booleans or tuples. Not a list, e.t.c

### Declaration

#### Approach 1

```py
D = {
    'name': 'Sifu',
    'age': 19,
    'job': 'Engineer'
}
```

​

#### Approach 2: using dict()

```py
# Create a dictionary with a list of two-item tuples
L = [
    ('name', 'Sifu'),
    ('age', 19),
    ('job', 'Engineer')
]
​
D = dict(L)
>>> D
# { 'name': 'Sifu', 'age': 19, 'job': 'Engineer' }
```

### Access Dictionary Items

```py
D = {
    'name': 'Sifu',
    'age': 19,
    'job': 'Engineer'
}
​

>>> D['name'] # Sifu
>>> D['salary'] # KeyError: salary
```

If you refer a key that doesn't exist it will throw an exception

To avoid such exception, you can use the special dictionary get() method. This method returns the value for key if key is in the dictionary, else None, so that this method never raises a KeyError.

```py
>>> D['salary'] # KeyError: salary
>>> D.get('name') # Sifu

>>> D.get('salary') # None
>>> D.get('salary', 'Not Found') # If doesn't exist return a default
# 'Not Found'
```

### Check if a Key or Value Exists

```py
>>> 'name' in D # True
>>> 'career' in D # False
```

### Value exists using values(),

```py
>>> 'Sifu' in D.values() # True
>>> 'Dingo' in D.values() # False
```
