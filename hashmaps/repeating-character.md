# Repeating Character

**First repeating character**

Given a string str, create a function that returns the first repeating character. If such character doesn't exist, return the null character '\0'.

**Examples**

_Input: str = "inside code"  -&gt; 'i'_

_Input: str = "programming"  -&gt; 'r'_

_Input: str = "abcd"  -&gt; '\0'_

```python
def firstRepeatingCharacter(s):
    seen = set()
    
    for char in s:
        if char in seen:
            return char
        
        seen.add(char)
        
    return '\0'
```

