## Modulus

Checks divisibility

### Even // Odd

```py
is_even = 17 % 2 == 0 # False
is_even = 12 % 2 == 0 # True

is_odd = 17 % 2 != 0 # True
is_odd = 12 % 2 != 0 # False
```

### Checking Truthy or falsy values

```py
not 17 # False
not 0 # True

not 'John' # False
not '' # True
```

### Even // Odd - Short form

```py
is_even = not 17 % 2 # False
is_even = not 12 % 2 # True

is_odd = 17 % 2 # True
is_odd = 12 % 2 # False

is_even = not 17 % 2
is_odd = 17 % 2
```

### divmod

```py
div, rem = divmod(17, 2)
# 17 // 2, 17 % 2

# 8, 1
```
