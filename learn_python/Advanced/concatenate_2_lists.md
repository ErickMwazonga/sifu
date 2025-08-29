# Concatenate 2 lists

Given 2 lists below, merge them into one list.

```
list1 = [1, 2, 3]
list2 = [4, 5, 6]
```

## 1. Using `+` Operator

```py
merged_list = list1 + list2
```

## 2. Using list `extend` method

```py
merged_list = list1.extend(list2)

# Alternatively
merged_list = []
merged_list.extend(list1)
merged_list.extend(list2)
```

## 3. Using inbuilt `sum` method

```py
all_list = [list1, list2]
merged_list = sum(all_list, [])
```

[Why does this work?](https://mathieularose.com/how-not-to-flatten-a-list-of-lists-in-python)

## 4. Using '\*' unpacking operator

```py
merged_list = [*list1, *list2]
```

## 5. Using Numpy `concatenate` method

```py
import numpy as np
all_lists = [list1, list2]
merged_list = list(np.concatenate(all_lists))
```
