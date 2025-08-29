## Range

1. range(end)
2. range(start, end)
3. range(start, end, step)
4. in-reverse

### range(end)

```py
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
idx  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# note:
start - inclusive
end - exclusive

range(end)
range(8)  -> [1, 2, 3, 4, 5, 6, 7]
```

### range(start, end)

```py
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
idx  = [0, 1, 2, 3, 4, 5, 6, 7, 8]

range(start, end) # no step, by default 1 is the step
range(2, 7)  -> [2, 3, 4, 5, 6]
```

### range(start, end, step)

```py
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
idx  = [0, 1, 2, 3, 4, 5, 6, 7, 8]

range(start, end, step)
range(2, 7, 2)  -> [2, 4, 6]
range(2, 7, 3)  -> [2, 5]
```

### in reverse

```py
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
idx  = [0, 1, 2, 3, 4, 5, 6, 7, 8]

N = len(nums) -> 9
nums[9]  -> Out of range
nums[9 - 1]  -> last item
nums[N - 1]

range(N - 1, -1, -1)
range(len(nums) - 1, -1, -1)
```
