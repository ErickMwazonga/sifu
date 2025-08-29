## String

The string module provides additional tools to manipulate strings.
Methods

```py
import string
​
>>> string.ascii_letters
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
​
>>> string.ascii_lowercase
# abcdefghijklmnopqrstuvwxyz
​
>>> string.ascii_uppercase
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
​
>>> string.digits
# 0123456789
​
>>> string.hexdigits
# 0123456789abcdefABCDEF
​
>>> string.whitespace
# ' \t\n\r\x0b\x0c'
​
>>> string.punctuation
# !"#$%&'()*+,-./:;?@[\]^_`{|}~
```

### `capwords()`

`Syntax - capwords(s, sep=None)`

Steps
This function split the specified string into words using str.split().
Then it capitalizes each word using str.capitalize() function.
Finally, it joins the capitalized words using str.join().

```py
>>> s = '  Welcome TO  \n\n JournalDev '
>>> string.capwords(s)
# 'Welcome To Journaldev'
```
