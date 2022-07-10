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

## Optional
`Optional[...]` is a shorthand notation for `Union[..., None]`, telling the type checker that either an object of the specific type is required, or None is required.

```py
from typing import Optional

def test(a: Optional[int] = None) -> Optional[int]:
    print(a)


test(1) # 1
test() # None


def test(a: Optional[list] = None) -> Optional[list]:
    print(a)

test([1, 2, 3]) # [1, 2, 3]
test() # None

# practical example
ID = Union[str, int] # str | int

def api_function(param: Optional[ID] = None) -> None:
    '''
    API STUB

    If param is given, it should be a string, or an integer is also accepted.
    Otherwise, it can be None
    '''
    ...

# From Python 3.9+ you are not required to use typing module:
def foo(bar: str = None):
    ....
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

## NoReturn
Sometimes functions never return, for example by always raising an exception. <br>
For such functions’ return types, we can “get away” with using None, but it’s best to use the special NoReturn type).

```py
from typing import Literal, NoReturn

def assert_never(value: NoReturn) -> NoReturn:
    assert False
```

## Constants - Final
### `typing.Final`
A special typing construct to indicate to type checkers that a name cannot be re-assigned or overridden in a subclass. 

```py
PORT: Final = 3000
PORT_NO: Final[int] = 22 # Explicitly definind data type
PORT = 4000  # Error reported by type checker

class Connection:
    TIMEOUT: Final[int] = 10
```