# Prefix Sum

## Turorials
1. 1D - https://www.youtube.com/watch?v=xbYr9JOC2Lk
2. 2D - https://www.youtube.com/watch?v=WibxoqMSMCw
3. https://www.hellointerview.com/learn/code/prefix-sum/overview

## 1D Prefix Sum
Quickly compute the sum of elements in a range [l, r] of an array.

### Computing prefix sum
```py
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

# Example
arr     = [2, 4, 5, 7]
prefix  = [0, 2, 6, 11, 18]
```

### Get range sum
```py
range_sum = prefix[r + 1] - prefix[l]

# Example
l, r = 1, 3
range_sum = prefix[r + 1] - prefix[l]  # 18 - 2 = 16
```

## 2D Prefix Sum (Matrix)
Quickly compute the sum of a submatrix from (r1, c1) to (r2, c2)

### Computing 2D prefix sum
```py
rows, cols = len(mat), len(mat[0])
prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        prefix[i][j] = mat[i - 1][j - 1] 
            + prefix[i - 1][j] 
            + prefix[i][j - 1]
            - prefix[i - 1][j - 1]

# Example
mat = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

# prefix will be:
# [
#   [0, 0,  0,  0],
#   [0, 1,  3,  6],
#   [0, 5, 12, 21],
#   [0,12, 27, 45]
# ]
```

### Get submatrix sum
```py
sub_sum = (
    prefix[r2 + 1][c2 + 1]
    - prefix[r1][c2 + 1]
    - prefix[r2 + 1][c1]
    + prefix[r1][c1]
)
```

## Difference Array
Instead of updating every value in a range (slow), just update boundaries and later compute cumulative values.

### Step-by-step:
Let’s say you want to add +10 from index 1 to 3:

Step 1: Add + substract boundaries
```py
res[0] += 10 (start of range)
res[3] -= 10 (one past the end)
```

Step 2: Later compute prefix sum:

This will cause all values between index 0 and 2 to have +10.

### example using prefix sum
```py
for i in range(1, n):
    result[i] += result[i - 1]

For bookings = [[1, 3, 10]], n = 5:
After difference step: [10, 0, 0, -10, 0]
After prefix sum: [10, 10, 10, 0, 0]
```

### Why It Works
- Efficient way to apply range updates in O(1)
- Final values are recovered with prefix sum

## Questions
### 1D Prefix Sums
// Easy - learning the concept
1. https://leetcode.com/problems/running-sum-of-1d-array
2. https://leetcode.com/problems/find-the-highest-altitude
3. https://leetcode.com/problems/find-the-middle-index-in-array
   
// Medium
1. https://www.hellointerview.com/learn/code/prefix-sum/count-vowels
2. https://leetcode.com/problems/count-vowel-strings-in-ranges
3. https://leetcode.com/problems/subarray-sum-equals-k
4. https://leetcode.com/problems/product-of-array-except-self/

// Difference array technique
1. https://algo.monster/liteproblems/370
2. https://leetcode.com/problems/corporate-flight-bookings
3. https://leetcode.com/problems/car-pooling