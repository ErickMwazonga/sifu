'''
969. Pancake Sorting
https://leetcode.com/problems/pancake-sorting/

Given an array of integers arr, sort the array by performing a series of pancake flips.
In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[1...k].
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1],
so arr = [1,2,3,4] after the pancake flip at k = 3.

Return the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts
the array within 10 * arr.length flips will be judged as correct.
'''


def flip(A, i):
    A[:i+1] = reversed(A[:i+1])


def findMaxUpTo(A, i):
    val = max(A[:i+1])
    return A.index(val)


def pancake_sort(arr):
    # start from the array and one by one reduce the current size
    curr_size = len(arr) - 1
    # find the index of the maxmium element inside the arr[0..curr_size -1]
    while curr_size > 0:
        max_index = findMaxUpTo(arr, curr_size)

        if max_index != curr_size:
            flip(arr, max_index)
            # now move the maximum number to the end by reversing current array
            flip(arr, curr_size)
        curr_size -= 1

    return arr


# print(pancake_sort([3,2,1,4]))
assert pancake_sort([3, 2, 1, 4]) == [1, 2, 3, 4]
