# D E F A U L T S

## 1. Default Values
## 1.1. `get()`
```py
data: dict[str, str] = {'Name': 'Zinga', 'Location': 'Migombani', 'Age': 33}
hobby: str = data.get('Hobbies', 'Coding')

print(hobby) # Coding
```
> **PROBLEM** - Sets default value for all missing keys


## 1.2. `setdefault()`
```py
data: dict[str, str] = {'Name': 'Zinga', 'Location': 'Migombani', 'Age': 33}
data.setdefault('Hobbies', None)

print(data['Hobbies']) # None
```
> **PROBLEM** - We need to know the key for which we want to create a default value beforehand


## 1.3. Custom default value
```py
from collections import defaultdict

ice_cream: dict[str, str] = defaultdict(lambda: 'Vanilla')

ice_cream['Cobih'] = 'Chunky Monkey'
ice_cream['Santa'] = 'Butter Pecan'

print(ice_cream['Cobih']) # Chunky Monkey
print(ice_cream['Chiwawa']) # Vanilla
```

## 2. Default Integers
## 2.1. Without defaultdict
```py
names: list[str] = [
    'Mchicha', 'Dingo', 'Evan', 'Mbenda', 'Sukari', 'Dingo', 'Mchicha'
]

freqs: dict[str, int] = {}

for name in names:
    # freqs[name] = freqs.get(name, 0) + 1

    if name in freqs:
        freqs[name] += 1
    else:
        freqs[name] = 1

print(freqs)
# {'Mchicha': 2, 'Dingo': 2, 'Evan': 1, 'Mbenda': 1, 'Sukari': 1}
```
## 2.2. With defaultdict
```py
from collections import defaultdict

names: list[str] = ['Nik', 'Kate', 'Evan', 'Kyra', 'John', 'Kate', 'Nik']

counts: dict[str, int] = defaultdict(int)
for name in names:
    counts[name] += 1

print(counts)
# defaultdict(<class 'int'>, {'Nik': 2, 'Kate': 2, 'Evan': 1, 'Kyra': 1, 'John': 1})
```

## 3. Default Lists
```py
# Resource: https://realpython.com/python-defaultdict/

Employee = tuple[str, str]

dep: list[Employee] = [
    ('Sales', 'John Fitina'),
    ('Sales', 'Martin Dungicha'),
    ('Accounting', 'Jane Kololeni'),
    ('Marketing', 'Elizabeth Mambo'),
    ('Marketing', 'Adam Wema')
]

from collections import defaultdict

mapping: dict[str, list] = defaultdict(list)
for department, employee in dep:
    mapping[department].append(employee)

    # [Code without default dict]
    # if department not in mapping:
    #     mapping[department] = []
    # mapping[department].append(employee)

# output
{
    'Sales': ['John Fitina', 'Martin Dungicha'],
    'Accounting' : ['Jane Kololeni'],
    'Marketing': ['Elizabeth Mambo', 'Adam Wema']
}
```