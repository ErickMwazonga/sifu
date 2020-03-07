def snail(arr):
    res = []

    def sort():
        # Return res for empty array
        if not len(arr):
            return res

        # Base case: Add the elements if only one row left
        if len(arr) < 2:
            return res.extend(arr[0])

        # Step 1: Add the first row to result, remove it from arr
        res.extend(arr.pop(0))

        # Step 2: Add the elements to result, remove them from arr
        for i in arr:
            el = i.pop()
            res.append(el)

        # Step 3: Add the last row to result in reverse, remove it from arr
        res.extend(reversed(arr[-1]))
        arr.pop()

        # Step 3: Add the first elements to result in reverse, remove them from arr
        for i in reversed(arr):
            el = i.pop(0)
            res.append(el)

        # Step 5: REPEAT
        sort()

    sort()    
    return res

# [[1,2,3], [4,5,6], [7,8,9]] = [1,2,3,6,9,8,7,4,5]
# [[1, 2, 3, 4], [ 5, 6, 7, 8], [ 9,10,11,12], [13,14,15,16]] 
# [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

a = [1]

b = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

c = [[1, 2, 3, 4],
     [ 5, 6, 7, 8],
     [ 9,10,11,12],
     [13,14,15,16]
    ]

print(snail(c))

