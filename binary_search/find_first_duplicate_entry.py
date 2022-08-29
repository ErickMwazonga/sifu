'''
Write a function that takes an array of sorted integers and a key and
returns the index of the first occurrence of that key from the array.

Example:
idx   0    1   2   3    4    5    6    7    8    9
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
Returns index 3 since 108 appears for the first time at
index 3.
'''


def find(nums, target):
    index = -1
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            index = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return index


A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
assert find(A, 108) == 3
