
def secDiagonal(A):
    res = []
    i, j = 0, len(A)-1
    
    while i < len(A) and j >= 0:
        res.append(A[i][j])
        i += 1
        j -= 1
    return res


a = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
assert secDiagonal(a) == [3, 5, 7]

b = [[1, 2, 3, 4],  [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
assert secDiagonal(b) == [4, 7, 10, 13]
