## Sort

### 1. Sort inplace

Syntax - `iterable.sort()`

```py
nums = [3, 5, 6, 1, 8]

sorted_nums = nums.sort()
sorted_nums  # Nothing since the list is updated in place
nums # [1, 3, 5, 6, 8]
```

### 2. Return a sorted list

Syntax - `new_list = sorted(iterable)`

```py
nums = [3, 5, 6, 1, 8]

sorted_nums = sorted(nums)
nums # won't be sorted -> [3, 5, 6, 1, 8]
sorted_nums # [1, 3, 5, 6, 8]
```

### 3. With `reverse` argument

```py
# By default reverse = False
names = ['Harry', 'Suzy', 'Al', 'Mark']
sorted(names)
# ['Al', 'Harry', 'Mark', 'Suzy']

sorted(names, reverse=True) # ['Suzy', 'Mark', 'Harry', 'Al']

nums = [6, 9, 3, 1]
sorted(nums, reverse=False) # same as `sorted(nums`
# [1, 3, 6, 9]

sorted(nums, reverse=True)
# [1, 3, 6, 9]
```

### With a `key` Argument

This argument expects a function to be passed to it, and that function will be used on each value in the list being sorted to determine the resulting order.

To demonstrate a basic example, let’s assume the requirement for ordering a specific list is the length of the strings in the list, shortest to longest. The function to return the length of a string, `len()`, will be used with the key argument:

```py
words = ['banana', 'pie', 'Washington', 'book']
sorted(words, key=len)
# ['pie', 'book', 'banana', 'Washington']

names_with_case = ['harry', 'Suzy', 'al', 'Mark']
sorted(names_with_case, key=str.lower)
# ['al', 'harry', 'Mark', 'Suzy']
```
