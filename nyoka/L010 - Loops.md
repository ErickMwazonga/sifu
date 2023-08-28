## Loops

### 1. For loop

```py
nums = list(range(10))

for num in nums:
    print(num)
```

### 2. While Loop

- Works with indexes
- Have an ending index, e.g loop till 100
- Break the loop

```py
nums = list(range(10))

i = 0
ending_position = len(nums) - 1 # 10 - 1 -> 9

while i <= ending_position:
    print(nums[i])


```

```py
nums = list(range(10)) # 10

i = 0
ending_position = len(nums)

while i < ending_position:
    print(nums[i])
```

### 3. Do while

- Inverted while loop

```py
nums = list(range(10)) # 10
i, ending_position = 0, len(nums)

do {
   print(nums[i])
}
while i < ending_position
```
