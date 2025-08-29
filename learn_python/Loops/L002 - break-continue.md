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
