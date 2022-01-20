'''
Rearrange array in zig-zag fashion

Given an array of DISTINCT elements, rearrange the elements of array in zig-zag fashion in O(n) time. 
The converted array should be in form a < b > c < d > e < f. 

Example:
Input: [4, 3, 7, 8, 6, 2, 1] 
Output: [3, 7, 4, 8, 2, 6, 1]

Input: [1, 4, 3, 2] 
Output: [1, 4, 2, 3]
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
