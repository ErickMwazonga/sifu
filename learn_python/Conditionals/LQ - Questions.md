### Questions

Q1 - Fizzbuzz - If num is divisible by 3 print FIZZ, if it's divisble by 5, print BUZZ, if it's divisible by 15 print FIZZBUZZ for numbers 1 to 50

If number is not 3/5/15, skip

```
Output:
    3 - FIZZ
    5 - BUZZ
    6 - FIZZ
```

```py
i, end = 1, 50

while i <= 50:
    if (i % 3 != 0) and (i % 5 != 0) and (i % 15 != 0):
        continue

    if i % 15 == 0:
        print(f'{i}-FIZZBUZZ')

    if i % 5 == 0:
        print(f'{i}-BUZZ')

    if i % 3 == 0:
        print(f'{i}-FIZZ')
```

```py
i, end = 1, 50

while i <= 50:
    if i % 15 == 0:
        print(f'{i}-FIZZBUZZ')
    if i % 5 == 0:
        print(f'{i}-BUZZ')
    if i % 3 == 0:
        print(f'{i}-FIZZ')
```
