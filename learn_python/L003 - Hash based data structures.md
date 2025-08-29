## Hash-based data structures

1. Set/Hashset
2. Dictionary/Hashmap

### Set

- Unordered collection of unique elements (no duplicates allowed).
- No index or position to access the element by its order.
- It doesn't maintain the prder of the elements
- Lookup is constant time -> faster
- Lookup in a list is linear time -> much slower

```py
nums = [2, 1, 3, 2, 4]
set(nums) -> unpredictable -> [2, 1, 3, 4]

def num_list(lst):
    seen = [] -> [2, 1, 3]
    for num in lst:
        if num in seen:
            return num
        else:
            seen.append(num)

    return -1

def num_list(lst):
    seen = [] -> [2, 1, 3]
    for num in lst:
        if num in seen:  -> linear time(slow) -> list
            return num

        seen.append(num)

    return -1

def num_list(lst):
    seen = set() -> [2, 1, 3]
    for num in lst:
        if num in seen:  -> constant time(faster) -> set
            return num

        seen.append(num)

    return -1
```
