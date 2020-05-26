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

from typing import List


def selection_sort(A: List) -> List:
    n = len(A)

    for step in range(n-1):
        min_index = step
        for i in range(step+1, n):
            if A[i] < A[min_index]:
                min_index = i

        A[step], A[min_index] = A[min_index], A[step]

    return A


data = [-2, 45, 0, 11, -9]
selection_sort(data)
assert data == [-9, -2, 0, 11, 45]
