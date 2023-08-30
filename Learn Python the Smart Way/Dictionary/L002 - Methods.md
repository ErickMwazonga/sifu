## Add and Update

### Add

If the key is new, it is added to the dictionary with its value.

```py
D = {
    'name': 'Sifu',
    'age': 19,
    'job': 'Engineer'
}

D['city'] = 'Nairobi'

>>> D
# {'name': 'Sifu', 'age': 19, 'job': 'Engineer', 'city': 'Nairobi'}
```

### Update

If the key is already present in the dictionary, its value is replaced by the new one.

```py
D = {
    'name': 'Sifu',
    'age': 19,
    'job': 'Engineer'
}

D['name'] = 'Dingo'

>>> D
# {'name': 'Dingo', 'age': 19, 'job': 'Engineer'}
```

### Merge Two Dictionaries

The `update()` method to merge the keys and values of one dictionary into another. Note that this method blindly overwrites values of the same key if there’s a clash.

```py
D1 = {
    'name': 'Sifu',
    'age': 19,
    'job': 'Engineer'
}

D2 = {
    'age': 30,
    'city': 'Nairobi',
    'email': 'sifu@ke.com'
}

D1.update(D2)

>>> D1
'''
 {
    'name': 'Sifu',
    'age': 30,
    'job': 'Engineer',
    'city': 'Nairobi',
    'email': 'sifu@ke.com'
}
'''
```

### Remove Dictionary Items

#### Get it's value

The `pop()` method removes the key and returns its value.

```py
D = {
    'name': 'Sifu',
    'age': 19,
    'job': 'Engineer'
}

x = D.pop('age')
>>> x # 19

>>> D
# {'name': 'Sifu', 'job': 'Engineer'}
```

#### Delete in place

```py
D = {
    'name': 'Sifu',
    'age': 19,
    'job': 'Engineer'
}

del D['age']
>>> D
# {'name': 'Sifu', 'job': 'Engineer'}
```

### Remove Last Inserted Item

The `popitem()` method removes and returns the last inserted item.

```py
D = {
     'name': 'Sifu',
     'age': 19,
     'job': 'Engineer'
}

x = D.popitem()
>>> x # ('job', 'Engineer')

>>> D
# {'name': 'Sifu', 'age': 19}
```

### Remove all Items

To delete all keys and values from a dictionary, use `clear()` method.

```py
D = {
    'name': 'Sifu',
    'age': 19,
    'job': 'Engineer'
}

D.clear()

>>> D
# {}
```
