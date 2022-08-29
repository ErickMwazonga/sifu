'''
Getting a Different Number

Given an array arr of unique nonnegative integers, implement a function 
getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn't have that restriction (like Python), 
assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, 
the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.
Solve first for the case when you're NOT allowed to modify the input arr. 
If successful and still have time, see if you can come up with an algorithm with an improved 
space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Examples:
1. [0, 1, 2, 3] -> 4 
2. [1000] -> 0
3. [0, 1, 3, 4] -> 2
'''


def getDifferentNumber(arr: list[int]) -> int:
    n = len(arr)
    arrSorted = sorted(arr)

    for i in range(n):
        if arrSorted[i] != i:
            return i

    return n


def getDifferentNumber_v2(arr):
    n = len(arr)
    hashset = set(arr)

    for i in range(n):
        if i not in hashset:
            return i

    return n


def getDifferentNumber_v3(arr):
    n = len(arr)
    temp = 0

    for i in range(n):
        temp = arr[i]
        while temp < n and arr[temp] != temp:
            temp, arr[temp] = arr[temp], temp

    for i in range(n):
        if arr[i] != i:
            return i

    return n
