## Conditionals

### One condition

```py
age = 34

if age >= 18:
	print('You can vote')
```

### Two condition

```py
age = 5

if age >= 18:
	print('You can vote')
else:
    print('You can't vote')
```

### More than two condition

```py
age = 5

if age <= 10:
	print('You are still a baby')
elif 10 < age < 18:
    print('You are a teen but not old enough to vote')
else:
    print('You can vote')
```
