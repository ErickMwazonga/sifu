## Dictionaries

Dictionaries are a collection of key-value pairs. They can be created using curly braces `{}` or the built in function

```py
scores = {
    'John': 89,
    'Peter': 23,
    'Montecalo': 76
}

nums = [1, 2, 1, 3, 4, 3, 1]
freqs = {
   1: 3,
   2: 1,
   3: 2,
   4: 1
}
```

Notes

- Key cannot be a mutable data type e.g list

### Looping

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

### Looping the key, value pairs similar to enumerate

```py
for key, val in freqs.items():
    print(f`{key} - {val}`)
```

### Defaults

```py
person = {
    name: 'Peter'
    age: 34
}

>>> person['school'] # KeyError

freqs = {}
if ch not in freqs:
    freqs[ch] = 1
else:
    freqs[ch] += 1
```

### 1. SetDefault

```py
freqs = {}
freqs.setdefault(0)

freqs[ch] += 1
```

### 2. get

```py
freqs = {
    1: 2,
    4: 3
}

freqs[ch] = freqs.get(ch, 0) + 1

freqs[5] = freqs.get(5, 0) + 1 -> 0 + 1 -> 1
freqs[4] = freqs.get(4, 0) + 1 -> 3 + 1 -> 4
```

### 3. defaultdict

- Used during dictionary initialization to set a default/fallback value

```py
from collections import defaultdict

freqs = defaultdict(int)
freqs[ch] = freqs[ch] + 1 # freqs[ch] += 1

freqs = defaultdict(list)
freqs[ch] = freqs[ch] + [99]

# not in freqs -> [99]
# in freqs    -> [87, 66, 99]
```
