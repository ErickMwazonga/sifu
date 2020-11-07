'''
Given a square matrix of order N*N,
write code to print all the elements in the order of their diagonal.
For example, in the below matrix, the elements should be printed in the marked (in red) order,
and the final output should be as shown below:

input
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
output
[1, 4, 2, 7, 5, 3, 8, 6, 9]

https://www.ritambhara.in/print-elements-of-a-matrix-in-diagonal-order/
https://www.youtube.com/watch?v=T8ErAYobcbc
'''

def findDiagonalOrder(matrix):
    res = []

    for k in range(n):
        i, j = k, 0

        while i >= 0:
            res.append(matrix[i][j])
            i -= 1
            j += 1

    for k in range(1, m):
        i, j = n - 1, k

        while j < m:
            res.append(matrix[i][j])
            i -= 1
            j += 1
    
