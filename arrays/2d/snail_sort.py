def snail(arr):
    res = []

    def sort():
        # Return res for empty array
        if not len(arr) or not len(arr[0]):
            return res

        # If every row contains on element
        if len(arr[0]) == 1:
            for i in range(len(arr)):
                res.append(arr[i][0])
            return res

        # Base case: Add the elements if only one row left
        if len(arr) <= 1:
            return res.extend(arr.pop(0))

        # Step 1: Add the first row to result, remove it from arr
        res.extend(arr.pop(0))

        # Step 2: Add the last elements to result, remove them from arr
        for i in arr:
            el = i.pop()
            res.append(el)

        # Step 3: Add the last row to result in reverse, remove it from arr
        res.extend(reversed(arr[-1]))
        arr.pop()

        # Step 4: Add the first elements to result in reverse,
        # remove them from arr
        for i in reversed(arr):
            el = i.pop(0)
            res.append(el)

        # Step 5: REPEAT
        sort()

    return res


b = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

c = [
    [1,  2,  3,   4],
    [5,  6,  7,   8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]

assert snail([1]) == [1]
assert snail([[7], [9], [6]]) == [[7], [9], [6]]
assert snail(b) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert snail(c) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]


def spiralOrder(matrix):
    res = []
    if len(matrix) == 0:
        return res

    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        # Step 1: Add the first row to result, remove it from arr
        for i in range(col_begin, col_end+1):
            res.append(matrix[row_begin][i])
        row_begin += 1

        # Step 2: Add the last elements to result, remove them from arr
        for i in range(row_begin, row_end+1):
            res.append(matrix[i][col_end])
        col_end -= 1

        # Step 3: Add the last row to result in reverse, remove it from arr
        if row_begin <= row_end:
            for i in range(col_end, col_begin-1, -1):
                res.append(matrix[row_end][i])
        row_end -= 1

        # Step 4: Add the first elements to result in reverse,
        if col_begin <= col_end:
            for i in range(row_end, row_begin-1, -1):
                res.append(matrix[i][col_begin])
        col_begin += 1

    return res


# INTERVIEW - MICROSOFT ON-SCREEN
# ---------------------------------
def visit_in_spiral(matrix):
	result = []
  
  if not len(matrix):
  	return matrix
  
  def spiral_helper(matrix):
  	# 1. first row
    first_row = matrix[0]
    result.extend(first_row)
    matrix.pop(0)
    
  	# 2. loop row 1 to n: print last item
    for i in range(0, len(matrix)):
        result.append(matrix[i].pop())
        
    # 3. last row in reverse
    for num in reversed(matrix[-1]): # -1 returns the last item
    	result.append(num)
      matrix.pop()
      
     # 4. first item of the remaining arrays
     for i in range(len(matrix)-1, -1, -1):
     	for j in range(0, len(matrix[0])):
      	result.append(num)
        matrix[i].pop(0)
    	
      if len(matrix):
      	spiral_helper(matrix)
    
    return result