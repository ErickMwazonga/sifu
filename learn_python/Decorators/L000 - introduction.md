## Introduction

### Articles

1. https://blog.stackademic.com/python-advanced-decorators-design-86f40ff2ffa3
2. https://codedamn.com/news/python/python-decorators-mastering-advanced-techniques-use-cases
3. https://www.youtube.com/watch?v=WpF6azYAxYg
4. https://www.youtube.com/watch?v=FsAPt_9Bf3U

### 1. Decorators with Arguments

Sometimes, you might want to pass arguments to your decorator. This can be achieved by using a higher-order function that returns a decorator:

```py
def logger_prefix(prefix):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'{prefix} Executing {func.__name__}')
            result = func(*args, **kwargs)
            return result

        return wrapper
    return decorator

@logger_prefix('[INFO]')
def say_hello(name):
    print(f'Hello, {name}!')

say_hello('Alice'))
```

### 2. Decorators that Maintain Metadata

When using decorators, it is important to maintain the metadata of the original function, such as its name and docstring. The functools.wraps decorator can be used to achieve this:

Using functools.wraps ensures that the metadata of the original function is preserved, making it easier to work with decorated functions.

```py
import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Executing {func.__name__}')
        result = func(*args, **kwargs)
        return result

    return wrapper

@logger
def say_hello(name):
    '''Greet someone by their name.'''
    print(f'Hello, {name}!')

print(say_hello.__name__)
print(say_hello.__doc__)
```

Decorated functions might lose their metadata.
The functools.wraps function can be used to ensure that the original function's metadata remains intact.

### 3. Chaining Decorators

Decorators can be applied in sequence, with each one building on top of the previous.
The order matters and can change the final outcome.

```py
def decorator_1(func):
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator_2(func):
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator_1
@decorator_2
def say_hello():
    print('Hello!')

say_hello()
```

### 4. Class-based Decorators

Instead of using functions, decorators can be designed using classes, offering more structure and the power of OOP (e.g., state persistence).

```py
class ClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Before the function call')
        result = self.func(*args, **kwargs)
        print('After the function call')
        return result

@ClassDecorator
def greet(name):
    print(f'Hi, {name}')

greet('Bob')
```

### 5. Decorators for Coroutines and Async Functions

Async functions and coroutines can also be decorated, but the decorator must be asynchronous as well

```py
import asyncio

def async_decorator(coro):
    async def wrapper(*args, **kwargs):
        print('Before the coroutine')
        await asyncio.sleep(1)
        result = await coro(*args, **kwargs)
        print('After the coroutine')
        return result
    return wrapper

@async_decorator
async def async_greet():
    print('Hello asynchronously!')

asyncio.run(async_greet())
```

### 6. Parameterized Decorators for Classes

These decorators accept arguments and can be applied to classes, affecting how the class or its methods work.

```py
def class_decorator(arg1, arg2):
    def inner_decorator(cls):
        class NewClass(cls):
            attribute1 = arg1
            attribute2 = arg2

        return NewClass

    return inner_decorator

@class_decorator('value1', 'value2')
class MyClass:
    pass

obj = MyClass()
print(obj.attribute1, obj.attribute2)
```
