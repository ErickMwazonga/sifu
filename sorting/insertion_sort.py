'''
Insertion Sort
Insertion sort is a sorting algorithm that places
an unsorted element at its suitable place in each iteration.

Worst: O(n2) -> sort in ascending order but the array is in descending.
Best: O(n) -> array is already sorted, the outer loop runs for n times
           -> whereas the inner loop does not run at all
Average: O(n2) -> elements of the array are in jumbled order.

Space: O(1) -> extra variable temp for min index.
'''

# ---------------------------------
# [BUCKET SORT] VS[INSERTION SORT]
# ---------------------------------


def insertionSort(A):
    n = len(A)

    for i in range(1, n):
        pos = i
        temp_val = A[i]

        while pos > 0 and A[pos-1] > temp_val:
            A[pos] = A[pos-1]
            pos -= 1

        A[pos] = temp_val


def insertion_sort(A: list) -> list:
    n = len(A)

    for step in range(1, n):
        key = A[step]
        j = step - 1

        # Compare key with each element on the left of it
        # until an element smaller than it is found
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1

        # Place key at after the element just smaller than it.
        A[j+1] = key


data = [9, 5, 1, 4, 3]
insertion_sort(data)
assert data == [1, 3, 4, 5, 9]
