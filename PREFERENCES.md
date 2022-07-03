## PREFENCES OF CODING STYLE

### Desclaimers
1. Variables used are assumed to be declared if not the point of interest

### Multiple variables' declaration(Inline Declaration)
Given two or more variables that need to be declared at ago `IFF`: <br/>
1. The variables are somehow related
2. The variables names do not pass the preferred length of a line(80 characters), otherwise do not use inline declaration.

```py
# recommended
i, j = 0, 0

# not recommended
i = 0
j = 0
```

### Increamenting multiple variables in a loop
```py
# recommended
while i < n and j < m:
    # logic...
    i, j = i + 1, j + 1

# not recommended
while i < n and j < m:
    # logic...
    i, j = i + 1, j + 1
```