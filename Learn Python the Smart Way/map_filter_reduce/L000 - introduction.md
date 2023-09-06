## Introduction

Map, Filter, and Reduce are paradigms of functional programming. <br>
They allow the programmer (you) to write simpler, shorter code, without neccessarily needing to bother about intricacies like loops and branching.

## Anonymous Functions/Lambda Functions

An anonymous method is a method without a name, i.e. not bound to an identifier like when we define a method using def method:.

## Syntax

What is the syntax of a lambda function (or lambda operator)?

`lambda arguments: expression`

## Example

```py
def add(x, y):
	return x + y

lambda x, y: x + y
```

## In sorting

### Syntax

`list.sort(key = none, reverse = false)`

`sorted(iterable, key function, reverse)`

### Example

```py
numbers = [2, 4, 1, 6, 3]
numbers.sort(key=lambda x: x)

# [1, 2, 3, 4, 6]

# Sort list of tuples
lst = [('Ann', '20', '400'), ('Scott', '40', '500'), ('Bean', '10', '450')]

lst.sort(key=lambda x: x[1])
print(lst)
# [('Bean', '10', '450'), ('Ann', '20', '400'), ('Scott', '40', '500')]
```
