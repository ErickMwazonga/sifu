## Reverse

### 1. Reverse inplace

```py
nums.reverse() # go to memeory and change the list reference

reversed_nums = nums.reverse()
reversed_nums  # Nothing since the list is updated in place
nums # reversed
```

### 2. Return a sorted list

```py
reversed_nums = reversed(nums)
nums # won't be reversed
reversed_nums # reversed
```
