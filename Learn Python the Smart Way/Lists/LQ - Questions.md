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
