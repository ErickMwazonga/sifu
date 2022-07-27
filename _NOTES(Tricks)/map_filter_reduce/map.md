# `map()`

Map, Filter, and Reduce are paradigms of functional programming. <br>
They allow the programmer (you) to write simpler, shorter code, without neccessarily needing to bother about intricacies like loops and branching.

It works with iterables to transform an existing elements of an iterable to a new list. <br/>
Syntax - `map(func, *iterables)`


## Single Iterable
### Example 1 - Square Items
Square elements in list by 2
```py
nums = [1, 2, 3, 4, 5]

# Loop
squared = []
for num in nums:
    squared.append(num**2)

# List comprehension
squared = [num**2 for num in nums]

# map()
squared = map(lambda num: num**2, nums)
squared= list(squared)
```

### Example 2 - Str to int
Convert integer-strings to integers
```py
nums = ['13', '17', '18', '21', '32']

# Loop
nums_ints = []
for num in nums:
    nums_ints.append(int(num))

# List comprehension
nums_ints = [int(num) for num in nums]

# map()
nums_ints = list(map(int, nums))
```

### Example 3 - Capitalize Strings
Capitalize each word in a list of strings
```py
names = ['bazeng', 'chiko', 'madanga']

# Loop
new_names = []
for name in names:
    new_names.append(name.capitalize())

# List comprehension
new_names = [name.capitalize() for name in names]

# map()
new_names = map(lambda name: name.capitalize(), names)
```

### Example 4 - Static Functions
```py
# absolute function
nums = [-2, -1, 0, 1, 2]
new_nums = list(map(abs, nums)) # [2, 1, 0, 1, 2]

# str to int
nums = ['13', '17', '18', '21', '32']
nums_ints = list(map(int, nums)) # [13, 17, 18, 21, 32]

# length of words
names = ['bazeng', 'chiko', 'madanga']
new_names = list(map(len, names)) # [6, 5, 7]

# square root
import math

nums = [4, 9, 16, 25, 36]
sqrt_nums = list(map(math.sqrt, nums)) # [2.0, 3.0, 4.0, 5.0, 6.0]
sqrt_nums_ints = list(map(int, sqrt_nums)) # [2, 3, 4, 5, 6]
```

## Multiple Iterables
### Example 1 - `Round()`
The `round()` built-in function takes two arguments -- the number to round up and the number of decimal places to round the number up to.

```py
areas = [3.56773, 5.57668, 4.00914, 56.24241, 32.00013]
decimal_places = range(1, 6)

new_areas = map(round, areas, decimal_places)
list(new_areas) # [3.6, 5.58, 4.009, 56.2424, 32.00013]
```

### Example 2 - `zip()`
The zip() function is a function that takes a number of iterables and then creates a tuple containing each of the elements in the iterables. 

```py
nums = [1, 2, 3, 4]
strings = ['a', 'b', 'c', 'd']

merge = zip(nums, strings)
list(merge) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
```

### Example 3 - `pow()`
```py
bases = [10, 20, 30, 40, 50]
index = [1, 2, 3, 4, 5]

powers = map(pow, bases, index)
list(powers) # [10, 400, 27000, 2560000, 312500000]
```

## Custom Function
### Square of elements
```py
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]

nums_squared = map(square, nums)
nums_squared_v2 =  map(lambda x: square(x), nums) 

list(nums_squared) # [1, 4, 9, 16, 25]
list(nums_squared_v2) # [1, 4, 9, 16, 25]
```

### Multiple iterables
```py
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

def getSum(x, y):
    return x + y

result = map(getSum, list1, list2)

# lambda function
result_v2 = map(lambda x, y: getSum(x, y), list1, list2)
result_v3 = map(lambda x, y: x + y, list1, list2)

list(result) # [7, 9, 11, 13, 15]
list(result_v2) # [7, 9, 11, 13, 15]
list(result_v3) # [7, 9, 11, 13, 15]
```