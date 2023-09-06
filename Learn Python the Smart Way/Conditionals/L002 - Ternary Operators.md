## Ternary Expressions

These operators evaluate something based on a condition being true or not.

### Syntax

`value_if_true if condition else value_if_false`

### Example

```js
// Javascript
const can_vote = true;
const vote_status = can_vote ? 'Go and vote' : 'Can't vote'
```

```py
# Python
can_vote = True
vote_status = 'Go and vote' if can_vote else 'Can`t vote'
```

## Short Circuit

### Syntax

```py
>>> True or 'HELLO' # True
>>> False or 'HELLO' # 'HELLO'

>>> output = None
>>> msg = output or 'No data returned'
>>> print(msg) # No data returned

def my_function(real_name, optional_display_name=None):
    optional_display_name = optional_display_name or real_name
    print(optional_display_name)

my_function('John') # John
my_function('Mike', 'anonymous123') #anonymous123
```
