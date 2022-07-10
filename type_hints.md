## Module

Module -> `python -m pip install mypy` <br>
Checking -> `mypy app.py`

## Basic type hinting
Let's start by using type hinting to annotate some variables that we expect to take basic types.

```py
name: str = 'Sifu'
age: int = 29
height: float = 1.87
python_is_great: bool = True
```

## Tuples
```py
from typing import Tuple

# For tuples of fixed size, we specify the types of all the elements
person: tuple[str, str, int] = ('Erick', 'Nairobi', 1990) # Python 3.9+
person_v2: Tuple[str, str, int] = ('Erick', 'Nairobi', 1990)

# For tuples of variable size, we use one type and ellipsis
people: tuple[str, ...] = ('Erick', 'Sifa', 'Willy')

# Using Alias
Person = list[tuple[str, str, int]]
people: Person = ('Erick', 'Nairobi', 1990)

people: list[Person] = [
    ('Erick', 'Nairobi', 1990),
    ('Chepe', 'Mombasa', 1971),
    ('Kabanga', 'Kisumu', 1963)
]
```

## Lists
```py
from typing import List

nums: list[int] = [1] # Python 3.9+
nums: List[int] = [1]
```

## Sets
```py
from typing import Set

nums: set[int] = {6, 7} # Python 3.9+
nums: Set[int] = {6, 7}
```

## Dictionaries
```py
from typing import Dict

x: dict[str, float] = {'Version': 2.0}  # Python 3.9+
x: Dict[str, float] = {'Version': 2.0}

from collections import defaultdict
mapping: dict[str, list] = defaultdict(list)
```

## TypedDict
It allows us to declare a structure for dicts, mapping their keys (strings) to the types of their values.
```py
from typing import TypedDict

class Person(TypedDict):
    name: str
    country: str
    jobs: list[str]


def get_people() -> Person:
    person: Person = {
        'name': 'Erick',
        'country': 'Kenya',
        'jobs': ['Software Engineer', 'Data Scientist'],
    }
    return person
```

## Functions Annotations
```py
def function_name(param1: type, param2: type) -> return_type:
    ...

# example
def changeLog(language: str, version: float) -> str:
    ...
```

## Adding type hints for multiple types
```py
from typing import Union

Number = Union[int, float]
Number_V2 = int | float # Python 3.10+

def add(x: Number, y: Number) -> Number:
    return x + y
```

## Type aliases
```py
from typing import Union

Number = Union[int, float]
Number_V2 = int | float
```

## None Type
```py
def demostrate(param: None) -> None:
    return param
```

## Inline - Multiple Variables' Declaration
### Without hinting
```py
a, b, c = 1, 2, 3
```

### With hinting
```py
# not working
a: int, b: int, c: int = 1, 2, 3

# working
a: int = 0; b: int = 1; c: int = 2
```