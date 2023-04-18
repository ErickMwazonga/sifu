'''
Given an array of integers arr and an integer num,
create a recursive function that returns the number of occurrences of num in arr

Example
input -> [4, 2, 7, 4, 4, 1, 2], num -> 4
output = 3
'''


def countOccurrences(arr: list[int], num: int, i: int = 0):
    if i == len(arr):
        return 0

    if arr[i] == num:
        return 1 + countOccurrences(arr, num, i+1)
    else:
        return countOccurrences(arr, num, i+1)


def countOccurrences_v2(arr: list[int], num: int, i: int = 0, acc: int = 0):
    if i == len(arr):
        return acc

    if arr[i] == num:
        return countOccurrences(arr, num, i+1, acc+1)
    else:
        return countOccurrences(arr, num, i+1, acc)
