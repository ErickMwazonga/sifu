## Indexing

```py
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pos  = [0, 1, 2, 3, 4, 5, 6, 8,...]
neg  = [              ..., -2, -1]

nums[5] -> 6
nums[-2] -> 8

nums[1:6] -> [2, 3, 4, 5, 6]
nums[1:8:3] -> [1, 4, 7]  -> 1 + 3 -> 4 + 3 etc

nums[1::] -> [1, + the rest]
nums[::-1] -> reverses
```
