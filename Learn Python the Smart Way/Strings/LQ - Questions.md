## Questions

### Q1 - Reverse a string

[Blog](https://vegibit.com/how-to-reverse-a-string-in-python/)

```py
def reverse_string_1(input_str: str) -> str:
    return input_str[::-1]

def reverse_string_2(input_str: str) -> str:
    reversed_str = ''
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_with_stack(input_str):
    stack = list(input_str)
    reversed_str = ''

    while stack:
        reversed_str += stack.pop()
    return reversed_str
```

### Q2 - Given a string, check if it's a palindrome

```py
'''
Examples

racecar -> True
mama -> False
madam -> True
'''

def is_palindrome_v1(string):
    return string == string[::-1]

def is_palindrome_v1(string):
    i, j =
```
