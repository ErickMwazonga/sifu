## Break//Continue

### In While loop

-> 1000 people
-> Print the first 20

```py
i, end = 0, 20
while i <= 20:
    print(f'Person {i}')
```

### Break

- terminate a loop before it ends

```py
i, end = 0, 1000
while i <= 1000:
    print(f'Person {i}')
    if i == 20:
        break # break out of while loop
        # return
```

### continue

- opposite of break, skips more procedural code after the expression

e.g. Given a list print only even numbers num % 2 == 0

```py
nums = list(range(20))
for num in nums:
    if num % 2 != 0:
        continue
    else:  # no need for else
        print(num)

for num in nums:
    if num % 2 != 0:
        continue

    new_num = num * 10
    print(new_num)
```

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
