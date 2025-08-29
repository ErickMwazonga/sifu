## Logical xor of two variables in Python?
-> [StackOverflow References](https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python)

### Explicit statement
`(a and not b) or (not a and b)`

### Bitwise Operation
`bool(a) ^ bool(b)`

### Bool Evaluation comparision
`bool(a) != bool(b)`

### Exlusive OR
`(a or b) and not (a and b)`

### Addition
`bool(a) + bool(b) == 1`


### `isdigit()` doesn't check for negative numbers
```python
>>> '2'.isdigit() # True
>>> '-2'.isdigit() # False
```
