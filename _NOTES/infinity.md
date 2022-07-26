# Infinity
## 1. Using `float('inf')` and `float('-inf)`
```py
positive_infinity = float('inf') # inf
negative_infinity = float('-inf') # -inf
```

## 2. Using Python’s math module
```py
import math
 
positive_infinity = float('inf') # inf
negative_infinity = float('-inf') # -inf
```

## 3. Integer `maxsize`
```py
import sys

maxSize = sys.maxsize # 9223372036854775807
minSize = -sys.maxsize # -9223372036854775807
```

## 4. Using Python’s decimal module
```py
from decimal import Decimal
 
positive_infinity = Decimal('Infinity') # Infinity
negative_infinity = Decimal('-Infinity') # -Infinity
```