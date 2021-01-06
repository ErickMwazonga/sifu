'''
CHALLENGE: COUNTING INVERSIONS
If array is already sorted then inversion count is 0.
If array is sorted in reverse order that inversion count is the maximum.
GENERALLY two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
'''

# REVISIT MERGE SORT
def mergeSort(A):
    n = len(A)

    if n < 2:
        return A

    mid = n // 2
    L, R = A[:mid], A[mid:]

    mergeSort(L)
    mergeSort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements of L[]
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    # Copy any remaining elements of R[]
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

def countInversions(A):
    n = len(A)

    if n < 2:
        return 0

    mid = n // 2
    left_half, right_half = A[:mid], A[mid:]

    left_inversion_count = countInversions(left_half)
    right_inversion_count = countInversions(right_half)

    i = j = k = 0
    inversion_count = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            A[k] = left_half[i]
            i += 1
        else:
            A[k] = right_half[j]
            j += 1
            # Count left elements after the current as inversions since
            # they are greater than current right element
            inversion_count += len(left_half) - i
        k += 1

    while i < len(left_half):
        A[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        A[k] = right_half[j]
        j += 1
        k += 1

    return inversion_count + left_inversion_count + right_inversion_count


assert countInversions([2, 4, 3, 1, 5]) == 4
assert countInversions([1, 20, 6, 4, 5]) == 5
