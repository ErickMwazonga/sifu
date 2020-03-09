"""
Selection Sort
The selection sort algorithm sorts an array by repeatedly finding the minimum element 
(considering ascending order) from unsorted part and putting it at the beginning.
The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order)
from the unsorted subarray is picked and moved to the sorted subarray.

Time Complexity: O(n2) as there are two nested loops.

Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps 
and can be useful when memory write is a costly operation.
"""

def selection_sort(A):
    n = len(A)

    for i in range(n-1):
        _min = i
        for j in range(i+1, n):
            if A[j] < A[_min]:
                _min =  j
        A[i], A[_min] = A[_min], A[i] 
    
    return A

a = [3, 5, 1, 6, 9, 2]
assert selection_sort(a) == [1, 2, 3, 5, 6, 9]



