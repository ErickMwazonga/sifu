## Check Data Type

### `isinstance`

The `isinstance()` function checks if the object argument is an instance or subclass of classinfo class argument.

### Syntax

`isinstance(object, classinfo)`

### Usage

Data type examples
[int, float, str, list, dict, tuple, set, ...]

```py
num = 80
>>> isinstance(num, int) # True
>>> isinstance(num, float) # False
​
PI = 3.14
>>> isinstance(PI, float) # True
​
# Check if 'sifula.com' is an instance of class string
domain = "sifula.com"
>>> isinstance(domain, str) # True
​
# Check if names is an instance of class list
names = ['Zinga', 'Rimba', 'Kelly"]
>>> isinstance(names, list) # True
```

### `type()`

The `type()` function either returns the type of the object or returns a new type object based on the arguments passed.

```py
>>> nums = [1, 2]
>>> print(type(nums))
# <class 'list'>
​
>>> freqs = { 1: 'one', 2: 'two' }
>>> type(freqs))
# <class 'dict'>
```
