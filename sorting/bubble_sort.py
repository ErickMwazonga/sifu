from typing import List

'''
BUbble Sort:
It compares the adjacent elements and
swaps their positions if they are not in the
intended order iteratively until they are sorted.

Worst: O(n2) -> sort in ascending order but the array is in descending.
Best: O(n) -> rray is already sorted,.
Average: O(n2) -> elements of the array are in jumbled order.

Space: O(1) -> extra variable temp for swapping.
'''


def bubbleSort(A: List) -> List:
    length = len(A)

    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True

        # if there is not swapping in the last swap,
        # then the array is already sorted.
        if not swapped:
            break


data = [-2, 45, 0, 11, -9]
bubbleSort(data)
assert data == [-9, -2, 0, 11, 45]
