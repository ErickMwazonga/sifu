## Type Casting

The process in which we convert a literal of one type to another.

| Method     | Casting                                                                |
| ---------- | ---------------------------------------------------------------------- |
| `int()`    | Convert float or string literal to a int.                              |
| `float()`  | Convert int or string literal to a float.                              |
| `str()`    | Convert a float or int literal to a a str.                             |
| `bool()`   | Convert any data type to boolean data.                                 |
| `tuple(x)` | Converts y to a tuple.                                                 |
| `list(x)`  | Converts y to a list.                                                  |
| `set(x)`   | Converts y to a set.                                                   |
| `dict(x)`  | Creates a dictionary and y should be a sequence of (key,value) tuples. |

## Int Conversion

### float to int

```py
num = 100.05
​
n = int(num)
>>> n  # 100
>>> type(n) # <class 'int'>
```

### string to int

```py
s = '132'
​
n = int(s)
>>> n # 132
>>> type(n) # <class 'int'>
```

> If the string has decimal point, then convert it to a float before converting it to int i.e. int(float(s))

### Float Conversion

### int to float

```py
n = 100
​
f = float(n)
>>> f  # 100.0
>>> type(f) # <class 'float'>
```

### string to float

```py
s = '132.65'
​
f = float(s)
>>> f # 132.65
>>> type(f) # <class 'float'>
```

### String Conversion

### int to string

```py
n = 100
​
s = str(n)
>>> s  # '100'
>>> type(s) # <class 'str'>
```

### float to string

```py
num = 100.05
​
# to string
s = str(num)
>>> s # '100.05'
>>> type(s)  # <class 'str'>
```

### Boolean Conversion

```py
>>> bool(0) # False
>>> bool(1) # True
>>> bool(10) # True
>>> bool(0.13332) # True
>>> bool('Apple') # True
>>> bool('') # False
```
