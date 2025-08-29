'''
Bubble Sort

It compares the adjacent elements and
swaps their positions if they are not in the
intended order iteratively until they are sorted.

Worst: O(n2) -> sort in ascending order but the array is in descending.
Best: O(n) -> array is already sorted,.
Average: O(n2) -> elements of the array are in jumbled order.

Space: O(1) -> extra variable temp for swapping.
'''


def bubbleSort(A: list):
    n = len(A)

    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


def bubbleSort_v2(A: list):
    n = len(A)

    for i in range(n):
        for j in range(i, n-1):
            if A[j+1] < A[j]:
                A[j], A[j+1] = A[j+1], A[j]


def bubbleSort_v3(A: list):
    '''Optimization: What if the array is sorted after first swap?'''

    n = len(A)

    for i in range(n):
        swapped = False

        for j in range(i, n-1):
            if A[j+1] < A[j]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True

        if not swapped:
            break


def bubbleSort_v4(A: list):
    n = len(A)
    unsorted_until_index = n - 1

    for i in range(n):
        swapped = False

        # Last i elements are already in place
        # for j in range(0, n-i-1):
        for j in range(0, unsorted_until_index):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True

        unsorted_until_index -= 1

        # if there is not swapping in the last swap,
        # then the array is already sorted.
        if not swapped:
            break


data = [-2, 45, 0, 11, -9]
bubbleSort(data)

assert data == [-9, -2, 0, 11, 45]
