## Binary Search

### Context

```py
                 2           5
# nums = [13, 5, 18, 23, 45, 67], elem = 45
# nums = [3, 5, 8, 23, 45, 67], elem = 45

def find_elemenet(nums, elem):
    for num in nums:
        if num == elem:
            return True

    return False
```

### Binary search

- Sorted array/iterables
- Divide and conquer algorithm

```py
'''
https://leetcode.com/problems/binary-search/submissions/

# List not sorted -> loop every element O(n) - slower
# List is sorted -> continously split the array into half O(logn) - faster
         i         mid          j
# nums = [3, 5, 8, 23, 45, 67, 89], elem = 5
mid = 23
[3, 5, 8] or [45, 67, 89]
i      j


i      j <- j
[3, 5, 8]

[3, 5, 8, 23, 45, 67] -> 23
[23, 45, 67] -> 45
'''

def find_element(nums, elem):
    i, j = 0, len(nums)

    while i < j:
        mid = (i + j) // 2

        if nums[mid] == elem:
            return True # found it!

        if nums[mid] < elem:
            i = mid + 1
            # j remains the same
        else:
            # i remains the same
            j = mid

    return False

```
