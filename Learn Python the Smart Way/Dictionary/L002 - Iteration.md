## Get All Keys, Values and Key:Value Pairs

There are three dictionary methods that return all of the dictionary’s keys, values and key-value pairs: keys(), values(), and items().

```py
D = {
    'name': 'Sifu',
    'age': 19,
    'job': 'Engineer'
}
```

### 1. Get all keys

```py
>>> list(D.keys())
# ['name', 'age', 'job']
```

### 2. Get all values

```py
>>> list(D.values())
# ['Sifu', 19, 'Engineer']
```

### 3. Get all pairs

```py
>>> list(D.items())
# [('name', 'Sifu'), ('age', 19), ('job', 'Engineer')]
```

## Looping

### Looping the keys

```py
for key in freqs.keys():
    print(f`{key} - freqs[key]`)
```

### Looping the values

```py
for val in freqs.values():
    print(val)
```

### Looping the key, value pairs similar to `enumerate`

```py
for key, val in freqs.items():
    print(f`{key} - {val}`)
```
