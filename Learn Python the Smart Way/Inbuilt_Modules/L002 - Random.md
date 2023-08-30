## Random

The random module is a built-in module to generate the pseudo-random variables.

### Importing

```py
>>> import random
```

### Generate Random Floats

The `random.random()` method returns a random float number between 0.0 to 1.0.

```py
>>> random.random()
0.125234684807533
```

### Generate Random Integers

The random.randint() method returns a random integer between the specified integers.

```py
>>> random.randint(1, 100) # 15
>>> random.randint(1, 100) # 19
```

### Generate Random Numbers within Range

The `random.randrange()` method returns a randomly selected element from the range created by the start, stop and step arguments.

```py
>>> random.randrange(1, 10) # 6
>>> random.randrange(1, 10, 2) # 5
>>> random.randrange(0, 101, 10) # 80
```

### Select Random Elements

The `random.choice()` method returns a randomly selected element from a non-empty sequence.

```py
>>> random.choice('computer') # 't'
>>> random.choice([12, 23, 45, 67, 65, 43]) # 45
>>> random.choice((12, 23, 45, 67, 65, 43)) # 67
```

### Pick several elements

The `random.sample()` pick more than one element from a list or sequence.

```py
>>> myList = ['bmw', 'volvo', 'toyota', 'chrysler']
>>> random.sample(myList, 2)
# ['toyota', 'volvo']
```

### Shuffle Elements Randomly

The `random.shuffle()` method randomly reorders the elements in a list.

```py
>>> numbers=[12, 23, 45, 67, 65, 43]
>>> random.shuffle(numbers)
>>> numbers
[23, 12, 43, 65, 67, 45]
​
>>> random.shuffle(numbers)
>>> numbers
[23, 43, 65, 45, 12, 67]
```
