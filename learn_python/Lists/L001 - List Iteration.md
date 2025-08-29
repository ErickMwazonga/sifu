## List iteration

### 3 ways to iterate

```py
# 1 - for loop
nums = [1, 2, 3, 4]

for num in nums:
    print(num)

# 2 - Using range indexes
for i in range(len(nums)):
    print(nums[i])

# 3 - enumerate
for i, num in enumerate(nums):
    print(f`{i} - {num}`)
```

## Iterate in reverse

### 4 ways to iterate in reverse

```py
# 1 - for loop
nums = [1, 2, 3, 4]

for num in reversed(nums):
    print(num)

# 2 - Using range indexes
for num in nums[::-1]:
    print(num)

# 3 - Using range indexes
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])

# 4 - enumerate
for i, num in enumerate(nums[::-1]):
    print(f`{i} - {num}`)

for i, num in enumerate(reversed(nums)):
    print(f`{i} - {num}`)
```

## Merge 2 lists

```py
names = ['Senyo', 'Peter', 'Erick']
ages = [45, 98, 12, 65]

N, M = len(nums), len(ages)

shortest_len = N if N < M else M
for i in range(shortest_len):
    print(f`{names[i]} - {ages[i]})

# ZIP
for name, age in zip(names, ages):
    print(f'{name} - {age}')
```
