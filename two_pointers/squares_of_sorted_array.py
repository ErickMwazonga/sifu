'''
977. Squares of a Sorted Array
Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number,also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''

def sortedSquares(A):
    res = []
    
    i, j = 0, len(A) - 1
    
    while i <= j:
        if abs(A[i]) > abs(A[j]):
            _sq = A[i] ** 2
            res.insert(0, _sq)
            i += 1
        else:
            _sq = A[j] ** 2
            res.insert(0, _sq)
            j -= 1
    
    return res