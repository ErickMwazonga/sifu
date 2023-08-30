
# `Sort Iterables`
## Syntax
`sort()` and `sorted()` hav two optional parameters:<br>
1. `reverse` - If True, the sorted list is descending order<br> 
2. `key` - function that serves as a key for the sort comparison<br> <br> 

## Sort in place - `sort()`
```py
prime: list[int] = [11, 3, 7, 5, 2]
prime.sort()

print(prime) # [2, 3, 5, 7, 11]
```

## Sort to a different variable - `sorted()`
```py
prime: list[int] = [11, 3, 7, 5, 2]
new_prime: list[int] = sorted(prime)

print(new_prime) # [2, 3, 5, 7, 11]
```

## Sort the list in Descending order
```py
vowels: list = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)

print(vowels) # ['u', 'o', 'i', 'e', 'a']
```

## Sort with custom key function
```py
# Sort by lenth of strings in a list
list.sort(key=len)
sorted(list, key=len)

e.g.
words: list[str] = ['pinapples', 'grape', 'apples', 'mangoes']
sorted(words, key=len) # ['grape', 'apples', 'mangoes', 'pinapples']
```

## Sort a list of list by sum
```py
ListItem = list[int]

nums: list[ListItem] = [[7, 9], [2, 4], [8, 1], [5, 6]]
sorted(nums, key=sum) # [[2, 4], [8, 1], [5, 6], [7, 9]]
```

## Sort dictionary
```py
sorted_dict = sorted(d.items(), key=lambda x: x[1])
sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
sorted_dict = dict(sorted_dict)
```
## Sorting dictionary by the first index is the default sorting mechanism
```py
nums = [[7, 9], [2, 4], [8, 1], [5, 6]]
sorted_nums = sorted(nums, key=lambda x: x[0])
sorted_list = sorted(nums)

assert sorted_nums == sorted_list # TRUE

# Alternatively
sorted(d, key=d.get, reverse=True):

# Examples
employees = [
    {'Name': 'Sifu', 'age': 25, 'salary': 10000},
    {'Name': 'Chepe', 'age': 30, 'salary': 81000},
    {'Name': 'Ericko', 'age': 18, 'salary': 110000},
]

employees.sort(key=lambda x: x.get('Name'))
employees.sort(key=lambda x: x.get('salary'), reverse=True)
```

## Sorting Algorithms(Major)
### Time Complexities
| Algorithm	     | Time Complexity	 | Space Complexity |
|----------------|-------------------|------------------| 
| Selection Sort | O(n^2)            | O(1)             |
| Bubble Sort    | O(n^2)            | O(1)             |
| Insertion Sort | O(n^2)            | O(1)             |
| Quick Sort     | O(n^2)            | O(log(n))        |
| Heap Sort      | O(n log(n))	     | O(1)             |
| Merge Sort     | O(n log(n))	     | O(n)             |
| Heap Sort      | O(n log(n))	     | O(1)             |