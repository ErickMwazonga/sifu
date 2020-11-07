'''
1594. Maximum Non Negative Product in a Matrix
You are given a rows x cols matrix grid. Initially, you are located at the top-left corner (0, 0),
and in each step, you can only move right or down in the matrix.
Among all possible paths starting from the top-left corner (0, 0)
and ending in the bottom-right corner (rows - 1, cols - 1), 
find the path with the maximum non-negative product.
The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 10^9 + 7. If the maximum product is negative return -1.
Notice that the modulo is performed after getting the maximum product.

Example 1:
Input: grid = [[-1,-2,-3],
               [-2,-3,-3],
               [-3,-3,-2]]
Output: -1
Explanation: It's not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

Example 2:
Input: grid = [[1,-2,1],
               [1,-2,1],
               [3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).

Example 3:
Input: grid = [[1, 3],
               [0,-4]]
Output: 0
Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).

Example 4:
Input: grid = [[ 1, 4,4,0],
               [-2, 0,0,1],
               [ 1,-1,1,1]]
Output: 2
Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).
 
Constraints:
1 <= rows, cols <= 15
-4 <= grid[i][j] <= 4
'''

def maxProductPath(grid):
    '''
    time: O(M * N), space: O(M * N)
    '''
    
    if not grid:
        return -1
    
    n, m = len(grid), len(grid[0])
    
    # Construct matrix
    dp_max = [[1 for j in range(m)] for i in range(n)]
    dp_min = [[1 for j in range(m)] for i in range(n)]
    
    # Fill in topmost left
    dp_max[0][0] = dp_min[0][0] = grid[0][0]
    
    # Fill first rows
    for j in range(1, m):
        dp_max[0][j] = dp_min[0][j] = dp_max[0][j - 1] * grid[0][j]
        
    # Fill first cols
    for i in range(1, n):
        dp_max[i][0] = dp_min[i][0] = dp_max[i - 1][0] * grid[i][0]

    # Inner matrix
    for r in range(1, n):
        for c in range(1, m):
            curr_val = grid[r][c]
            _prods = (
                dp_max[r-1][c] * curr_val,
                dp_max[r][c-1] * curr_val,
                dp_min[r-1][c] * curr_val,
                dp_min[r][c-1] * curr_val
            )
            
            dp_max[r][c] = max(_prods)
            dp_min[r][c] = min(_prods)

    if dp_max[n-1][m-1] < 0:
        return -1
    
    return dp_max[n-1][m-1] % (10**9+7)