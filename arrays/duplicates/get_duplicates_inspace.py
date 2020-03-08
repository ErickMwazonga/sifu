
def duplicatePositions(arr):
    res = []

    for v in arr:
        pos = abs(v) - 1

        if arr[pos] < 0:
            res.append(pos + 1)
        
        arr[pos] = -nums[pos]
    
    return res


nums = [4, 3, 2, 7, 8, 2, 3, 1] # Output: [2, 5, 3]
print(duplicatePositions(nums))
