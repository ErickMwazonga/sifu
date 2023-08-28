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

### 3 ways to iterate

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

## Ternary Expressions

```js
// Javascript
const can_vote = true;
const vote_status = can_vote ? 'Go and vote' : 'Can't vote'
```

```py
# Python
can_vote = True
vote_status = 'Go and vote' if can_vote else 'Can`t vote'
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

## Questions

### Q1 - Given a list, return then number that is repeated

```py
nums = [1, 2, 3, 4, 2, 5, 6] -> 2
nums = [1, 2, 3, 4, 9, 5, 6] -> -1

BIG-O - Nˆ2

def num_list(nums):
    for num in lst:
        num = str(num)
        if lst.count(num) > 1:
            num = int(num)
            return num
    return -1
```

### Q2 - Given 2 sorted lists, create another list with sorted elements

```py
a = [0, 10, 20, 30]
b = [5, 18, 25, 45]

merged_list = [0, 5, 10, 18, 20, 25, 30, 45]

def merge_two_lists(a, b):
    return sorted([a + b])

a = []
b = [2, 3, 4]


merged_list = [0, 5, 10, 18, 20, 25, 30, 45]

def merge_two_lists(a, b):
    '''
    a = [0, 10, 20, 30] - 4
                        i
    b = [5, 18, 25, 45, 67, 98] - 6
                     j

    x  = [0, 5, 10, 18, 20, 25, 30]
    '''

    merged_list = []

    i, N = 0, len(a)
    j, M = 0, len(b)

    while i < N and j < M: # loop until atleast one list is exhausted
        if a[i] < b[j]:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[j])
            j += 1

    merged_list.extend(a[i:])
    merged_list.extend(b[j:])
```
