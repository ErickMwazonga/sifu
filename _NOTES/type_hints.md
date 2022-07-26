## Introduction
Python is a dynamic language, hence it doesn't force the user to enforce the type of the objects. <br/>
This can lead to bugs, and errors will be hard to find.<br/>

### **Solution**
Python can be used in conjunction with various other tools and implement features of static type checking along with its own Duck Typing.

### **Static Typed Language**
The type checking of the variable type is done at compile-time. <br/>
Also, the type system of the language forces to explicitly declare the 'data-type' of the variable before its usage.

### **Dynamic Typed Language**
The type checking of the variable type is done at run-time. <br/>
Also, the type system of the language doesn't force to explicitly declare the 'data-type' of the variable before its usage.

### **Duck typing in Python**
There is a popular principle in Python, 'If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.<br>
Simply the principle is saying that the types of object or class don't matter, but object needs to contains similar methods and properties, then the object can be used for a particular purpose.<br>
Let's look at an example to clarify the above statement in more detail.

## Static Type checker
### `mypy`
`mypy` type check your program.py file and print out any errors it finds. <br>
Mypy will type check your code statically: 
> This means that it will check for errors without ever running your code, just like a linter.

Install -> `python -m pip install mypy`<br>
Checking -> `mypy app.py` <br /><br />

## Basic type hinting
Let's start by using type hinting to annotate some variables that we expect to take basic types.

```py
name: str = 'Sifu'
age: int = 29
height: float = 1.87
python_is_great: bool = True

# Example
def sum_two_numbers(num1: int, num2: int) -> int:
    sum: int = num1 + num2    
    return sum

sum_two_numbers(5, 10)
```

## Tuples
```py
from typing import Tuple, Any

# For tuples of fixed size, we specify the types of all the elements
person: tuple[str, str, int] = ('Erick', 'Nairobi', 1990) # Python 3.9+
person_v2: Tuple[str, str, int] = ('Erick', 'Nairobi', 1990)

# To specify a variable-length tuple of homogeneous type, use literal ellipsis, e.g. Tuple[int, ...]
people: tuple[str, ...] = ('Erick', 'Sifa', 'Willy')

# A plain Tuple is equivalent to Tuple[Any, ...], and in turn to tuple.
people: tuple[Any, ...] = ('Erick', 19, 'Nairobi')

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
from typing import Set, TypeAlias

nums: set[int] = {6, 7} # Python 3.9+
nums: Set[int] = {6, 7}

SetItem: TypeAlias = tuple[int, int]
nums_set: set[SetItem] = {(1, 2), (2, 3), (3, 4)}
```

## Dictionaries
```py
from typing import Dict

version: dict[str, float] = {'Version': 2.0}  # Python 3.9+
version: Dict[str, float] = {'Version': 2.0}

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
        'jobs': ['Software Engineer', 'Data Scientist']
    }
    return person
```

## None Type
```py
def demostrate(param: None) -> None:
    return param
```

## Any Type
A special kind of type is Any. <br>
Every data type is a type of the `Any` type.

```py
from typing import Any

nums: Any = None
nums = []          # OK
nums = 2           # OK
```

## Function Annotations
```py
def function_name(param1: type, param2: type) -> return_type:
    ...

# example
def changeLog(language: str, version: float) -> str:
    ...
```

## Optional Arguments
`Optional[...]` is a shorthand notation for `Union[..., None]`, <br />
telling the type checker that either an object of the specific type is required, or None is required.

```py
from typing import Optional

def player(name: str, start: Optional[str] = None) -> str:
    print(start)


player('Erick', 2022) # 2022
player('Erick') # None


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
    Otherwise, it can be None.
    '''
    ...

# From Python 3.9+ you are not required to use typing module:
def foo(bar: str = None):
    ....
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
from typing import Union, TypeAlias

Number = Union[int, float]
Number: TypeAlias = Union[int, float]

Number_V2 = int | float
Number_V2: TypeAlias = Union[int, float]
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
Sometimes functions never return, for example by always raising an exception. <br/>
For such functions' return types, we can `get away` with using None, but it’s best to use the special NoReturn type).

```py
from typing import Literal, NoReturn

def assert_never(value: NoReturn) -> NoReturn:
    assert False
```

## Constants
### `typing.Final`
A special typing construct to indicate to type checkers that a name cannot be re-assigned or overridden in a subclass. 

```py
PORT: Final = 3000
PORT_NO: Final[int] = 22 # Explicitly definind data type
PORT = 4000  # Error reported by type checker

class Connection:
    TIMEOUT: Final[int] = 10
```

## Literal
You can use Literal to indicate that value can be one of the provided literals. <br/>
Static type checkers will report an error when the value doesn't match one of the provided literals.
```py
from typing import Literal, TypeAlias

STATUS = Literal['ACTIVE', 'DISABLED']
# STATUS: TypeAlias = Literal['ACTIVE', 'DISABLED']


class User:
    def __init__(self, username: str, status: STATUS):
        self.username = username
        self.status = status

user = User('john@doe.com', 'CREATED')

'''
mypy example.py
example.py:12: error: Argument 2 to 'User' has incompatible type 'Literal['CREATED']';
expected 'Union[Literal['ACTIVE'], Literal['DISABLED']]'
Found 1 error in 1 file (checked 1 source file)
'''
```

### Literal with other types
```py
from typing import Literal, TypeAlias

PeriodChoices = Literal['latest', 'week', 'month', 'year']
PeriodChoices: TypeAlias = Literal['latest', 'week', 'month', 'year']

VALID_PERIODS: list[PeriodChoices] = ['latest', 'month', 'week', 'year', 'week']
```
