'''
Rearrange array in zig-zag fashion

Given an array of DISTINCT elements, rearrange the elements of array in zig-zag fashion in O(n) time. 
The converted array should be in form a < b > c < d > e < f. 

Example:
1. [4, 3, 7, 8, 6, 2, 1] -> [3, 7, 4, 8, 2, 6, 1]
2. [1, 4, 3, 2] -> [1, 4, 2, 3]
'''


def zig_zag(arr):
    i, n = 1, len(arr)

    while i < n:
        curr, prev = arr[i], arr[i-1]

        if i % 2 == 0:
            if prev < curr:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        else:
            if prev > curr:
                arr[i], arr[i-1] = arr[i-1], arr[i]

        i += 1

    return arr


assert zig_zag([1, 4, 3, 2]) == [1, 4, 2, 3]
assert zig_zag([4, 3, 7, 8, 6, 2, 1]) == [3, 7, 4, 8, 2, 6, 1]


def zig_zag_v2(arr):
    if not arr:
        return arr

    for i in range(len(arr)-1):
        if i % 2 == 0:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


assert zig_zag_v2([]) == []
assert zig_zag_v2([1, 2, 3, 4, 5, 6]) == [1, 3, 2, 5, 4, 6]
assert zig_zag_v2([5, 2, 1, 7, 9, 8]) == [2, 5, 1, 9, 7, 8]
assert zig_zag_v2([-2, 3, 3, -3]) == [-2, 3, -3, 3]
