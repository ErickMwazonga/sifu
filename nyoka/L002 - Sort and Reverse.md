## Sort

### 1. Sort inplace

```py
nums.sort() # go to memeory and change the list reference

new_list = nums.sort()
new_list  # Nothing since the list is updated in place
nums # sorted
```

### 2. Return a sorted list

```py
new_list = sorted(nums)
nums # won't be sorted
new_list # sorted
```

## Reverse

### 1. Reverse inplace

```py
nums.reverse() # go to memeory and change the list reference

new_list = nums.reverse()
new_list  # Nothing since the list is updated in place
nums # reversed
```

### 2. Return a sorted list

```py
new_list = reversed(nums)
nums # won't be reversed
new_list # reversed
```
