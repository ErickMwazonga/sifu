'''
498. Diagonal Traverse
https://leetcode.com/problems/diagonal-traverse/
https://leetcode.com/problems/diagonal-traverse/discuss/145195/python-solution-beats-100-using-bfs-just-like-maze-problem

Given a matrix of M x N elements (M rows, N columns),
return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation: visit link
'''

def findDiagonalOrder(matrix):
    n, m = len(matrix), len(matrix[0])

    if n == 0 or m == 0:
        return []

    row, col = 0, 0
    result = []

    # Execute m * n times circle, in order to fill m * n element into aimArr
    for i in range(n * m):
        result.append(matrix[row][col])

        '''
        According to this subject model, we can find some rules about index of matrix.
        For example, the sum of all moving up trajectory element can be divided by 2，
        and the sum of all moving down trajectory element can't be divided by 2
        '''
        if (row + col) % 2 == 0:
            # moving up
            # If col == n - 1, it's mean this position is last column, so, only row index must be increased
            if col == (m - 1):
                row += 1
            # If row == 0, it's mean this position is first row, so, only column index can be increased
            elif row == 0:
                col += 1
            # In this condition, in order to moving up, column index must be increased and row index must be decreased
            else:
                row -= 1
                col += 1
        else:
            # moving down
            # If row == m - 1, it's mean this position is last row, so, only column index must be increased
            if row == (n - 1):
                col += 1
            # If col == 0, it's mean this position is first column, so, only row index can be increased
            elif col == 0:
                row += 1
            # In this condition, in order to moving down, row index must be increased and column index must be decreased
            else:
                row += 1
                col -= 1
    
    return res