## Collections

Python collections module was introduced to improve the functionalities of the built-in collection containers.

```py
from collections import OrderedDict
​
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
​
>>> dict(od)
# {'a': 1, 'b': 2, 'c': 3}
```

### Deque

The deque is a list optimized for inserting and removing items.

```py
from collections import deque
​
list = ["a", "b", "c"]
deq = deque(list)
​
>>> deq
# deque(['a', 'b', 'c'])
```

### Inserting Elements

```py
>>> deq.append("d")
>>> deq.appendleft("e")
>>> deq

# deque(['e', 'a', 'b', 'c', 'd'])
```

### Removing Elements

```py
>>> deq.pop()
>>> deq.popleft()
>>> deq

# deque(['a', 'b', 'c'])
```

### Clearing a deque

```py
>>> deq.clear()
```

### Counting Elements

```py
>>> deq.count("a") # 1
>>> NamedTuple
>>> The namedtuple() returns a tuple with names for each position in the tuple. One of the biggest problems with ordinary tuples is that you have to remember the index of each field of a tuple object.
```

### Named Tuple

```py
>>> from collections import namedtuple
>>> Student = namedtuple('Student', 'fname, lname, age')
>>> s1 = Student('Sifu', 'Clarke', '13')
>>> s1.fname # Sifu
```

### Creating a namedtuple Using List

```py
>>> s2 = Student._make(['Dingo', 'Kaulu', '18'])
>>> s2
# Student(fname='Dingo', lname='Kaulu', age='18')
```

### Create a New Instance Using Existing Instance

```py
>>> s2 = s1._asdict()
>>> s2
# OrderedDict([('fname', 'Dingo'), ('lname', 'Kaulu'), ('age', '18')])
```
