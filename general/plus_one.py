# input -> Output
# [1, 2, 3] -> [1, 2, 4]
# [9, 9] -> [1, 0, 0]

def plus_one(arr):
    _str = '' .join(map(str, arr))
    res = str(int(_str) + 1)
    return [int(x) for x in res]

def plus_one_iteratively(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr        
        arr[i] = 0
    
    res = [0] * (len(arr) + 1)
    res[0] = 1
    return res



# print(plus_one([1, 2, 3]))
# print(plus_one([1, 2, 3]))
# print(plus_one_iteratively([1, 2, 3]))
print(plus_one_iteratively([9, 9, 9]))
print(plus_one_iteratively([1, 9, 9]))