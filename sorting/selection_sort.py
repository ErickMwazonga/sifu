"""
Selection Sort
Selection sort is an algorithm that selects
the smallest element from an unsorted list in each iteration
and places that element at the beginning of the unsorted list.

Worst: O(n2) -> sort in ascending order but the array is in descending.
Best: O(n2) -> array is already sorted,.
Average: O(n2) -> elements of the array are in jumbled order.

Space: O(1) -> extra variable temp for min index.
"""


def selection_sort(A):
    n = len(A)

    for i in range(n-1):
        min_index = i

        for j in range(i+1, n):
            if A[j] < A[min_index]:
                min_index = j

        A[i], A[min_index] = A[min_index], A[i]

    return A


data = [-2, 45, 0, 11, -9]
selection_sort(data)
assert data == [-9, -2, 0, 11, 45]
