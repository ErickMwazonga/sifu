'''
221. Maximal Square
https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

def maximalSquare(matrix):
    if not matrix or len(matrix) < 1:
        return 0
    
    n_rows, n_cols = len(matrix), len(matrix[0])
    
    dp = [[0] * (n_cols + 1) for _ in range(n_rows + 1)]
    max_side = 0
    
    for r in range(n_rows):
        for c in range(n_cols):
            if matrix[r][c] == '1':
                # Be careful of the indexing since dp grid has additional row and column
                dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                max_side = max(max_side, dp[r+1][c+1])
                
    return max_side * max_side