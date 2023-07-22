# Random
`random.randint(a, b)` -> a: inclusive, b: inclusive </br>
> coverage a <= n <= b </br>
Example
```py
import random
>>> [random.randint(1, 10) for _ in range(10)]
# [1, 8, **10**, 5, 9, 4, 6, 3, 5, 2]
```


`random.randrange(a, b)` -> a: inclusive, b: exclusive
> coverage a <= n < b </br>
Example
```py
import random
>>> [random.randrange(1, 10) for _ in range(10)]
# [1, 8, **9**, 5, 7, 4, 6, 3, 5, 2]
```
