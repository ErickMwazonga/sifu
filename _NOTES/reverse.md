# Reverse Iterables
## 1. By `reverse()`
It reverses an iterable in-place
```py
systems: list[str] = ['Windows', 'macOS', 'Linux']
systems.reverse()

print(systems) # ['Linux', 'macOS', 'Windows']
```

## 2. By Slicing -> `[::-1]`
```py
systems: list[str] = ['Windows', 'macOS', 'Linux']
reversed_list: list[str] = systems[::-1]
print(systems) # ['Linux', 'macOS', 'Windows']

# Printing Elements in Reversed Order
n: int = len(systems)
for i in range(n-1, -1, -1):
    print(systems[i])
```

## 3. By `reversed()`
```py
systems: list[str] = ['Windows', 'macOS', 'Linux']
reversed_systems: list[str] = reversed(systems)

print(list(reversed_systems)) # ['Linux', 'macOS', 'Windows']

# Printing Elements in Reversed Order
for system in reversed(systems):
    print(system)
```