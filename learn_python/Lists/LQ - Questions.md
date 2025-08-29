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

### Q3 - Second Largest Number

Largest number - Sorting

```py
def largest_number(lst: list[int]) -> int:
    return max(sorted(lst)) # nlogn
```

Largest number - Looping

```py
def largest_number(lst: list[int]) -> int:
    # largest = float('-inf')
    if not lst:
        return -1

    largest = lst[-1]
    for num in lst:
        if num > largest:
            largest = num

    return largest
```

What if all numbers in the list are negative

Second Largest number - Sorting

```py
def largest_number(lst: list[int]) -> int:
    if len(lst) > 1:
        return sorted(lst)[-2]
    return -1

    # return sorted(lst)[-2] if len(lst) > 1 else -1 # nlogn
```

'''
Largest number - Looping  
 [23, 15, 8, 45, 28, 34]
largest  
2 largest  
[]

- largest = -inf
- 2 largest = -inf

[23]

- largest = 23
- 2 largest = -inf

[-4, -45, -23, -1] -> -1

NOTE

- FIND MAXIMUM - should use -inf
- FINDING MINIMUM - should use inf

[23, 15, 8, 45, 28, 34]

largest
[] -> -1
[23] -> 23
[34, 23, 56, 12] -> 56

second largest
[] -> -1
[23] -> -1
[34, 67] -> 34

23

second_largest = 18
largest = 34

[34, 23, 56, 12, 45, 5, 24] -> 34
'''

```py
def second_largest_number(nums: list[int]) -> int:
    if not nums:
        return -1

    if len(nums) == 2:
        return min(nums)

    # largest, second_largest = nums[0], nums[0]
    # largest, second_largest = float('-inf'), float('-inf')

    second_largest, largest = float('-inf'), nums[0]

    for num in lst:
        # if num < largest and num < second_largest:
        if num < second_largest:
            continue

        if num > largest:
            # second_largest = largest
            # largest = num

            temp = largest
            largest = num
            second_largest = temp

        # if second_largest < num and second_largest < largest:
        if second_largest < num < largest:
            second_largest = num

    return second_largest

```
