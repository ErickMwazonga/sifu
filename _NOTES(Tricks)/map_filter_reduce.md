# **Map, Filter, Reduce**

Map, Filter, and Reduce are paradigms of functional programming. <br>
They allow the programmer (you) to write simpler, shorter code, without neccessarily needing to bother about intricacies like loops and branching.


## `map()`
It works with iterables to transform an existing elements of an iterable to a new list.


```py
iterator = map(fn, list)
Code language: Python (python)
In this syntax, fn is the name of the function that will call on each element of the list.

In fact, you can pass any iterable to the map() function, not just a list or tuple.

Back to the previous example, to use the map() function, you define a function that doubles a bonus first and then use the map() function as follows:
```