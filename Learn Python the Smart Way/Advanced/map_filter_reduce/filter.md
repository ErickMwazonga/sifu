# `Filter()`
The filter function passes each element of an iterable through a boolean function hence removing elements that returns false.

## Syntax
`filter(func, iterable)`

Notes:
1. Only one iterable is required.
2. The func returns a boolean type. If it doesn't, filter simply returns the iterable passed to it. 
3. The func MUST only take one argument.
4. `filter` passes each element in the iterable through func and returns only the ones that evaluate to true.

### Example 1 - Get A grades
```py
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score >= 80

a_grades = filter(is_A_student, scores)
list(a_grades) # [90, 88, 81]

# lambda function
a_grades_v2 = filter(lambda score: score >= 80, scores)
list(a_grades) # [90, 88, 81]
```

### Example 2 - Palindromes
```py
words = ['demigod', 'rewire', 'madam', 'freer', 'anutforajaroftuna', 'kiosk']

palindromes = filter(lambda word: word == word[::-1], words)
list(palindromes) # ['madam', 'anutforajaroftuna']
```

### Example 3 - Even Numbers
```py
nums = [1, 2, 3, 4, 5, 6, 7]

even_nums = filter(lambda x: x % 2 == 0), nums)
list(even_nums) # [2, 4, 6]
```