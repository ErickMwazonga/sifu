
# `str to int` <> `int to str`
## `ord()`
Returns an integer representing the Unicode character for your input string.
```py
>>> [ord(str(i)) for i in range(0, 10)]
# [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

>>> import string
>>> [ord(i) for i in string.ascii_uppercase] # [65 -> 90]
# [65, 66, ..., 90]

>>> [ord(i) for i in string.ascii_lowercase] # [97 -> 122]
# [97, 98, ..., 122]
```

### Getting a corresponding integer from an integer character
```py
>>> ch = '5'
>>> ord(ch) - ord('0') # 5
```

## `chr()`
Returns a character (a string) from an integer (represents unicode code point of the character)

```py
>>> val = 5 
# it's corresponding unicode is 53 = 48 + 5: ord('0') + 5

>>> val_repr = ord('0') + val
>>> char_rep = chr(val_repr) # 5
```
