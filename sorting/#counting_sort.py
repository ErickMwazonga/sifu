"""
Counting Sort
https://www.interviewcake.com/concept/python3/counting-sort
https://www.programiz.com/dsa/counting-sort
https://www.programiz.com/dsa/counting-sort
Counting sort is a sorting algorithm that sorts the elements
of an array by counting the number of occurrences of each unique
element in the array. The count is stored in an auxiliary array
and the sorting is done by mapping the count as an index of the auxiliary array.

Overall complexity = O(max)+O(size)+O(max)+O(size) = O(max+size)

Worst Case Complexity: O(n+k)
Best Case Complexity: O(n+k)
Average Case Complexity: O(n+k)
Space: O(1) -> O(max)
"""
from typing import List


# REVISTI
def counting_sort(A: List) -> List:
    size = len(A)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(size):
        count[A[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array
    # in count array and place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        A[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
counting_sort(data)
assert data == [1, 2, 2, 3, 3, 4, 8]
