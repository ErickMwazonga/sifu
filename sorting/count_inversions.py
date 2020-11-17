'''
CHALLENGE: COUNTING INVERSIONS
If array is already sorted then inversion count is 0.
If array is sorted in reverse order that inversion count is the maximum.
GENERALLY two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
'''

# REVISIT MERGE SORT
def mergeSort(A):
    n = len(A)

    if n == 1:
        return A

    mid = n // 2
    a, b = A[:mid], A[mid:]

    a = mergeSort(a)
    b = mergeSort(b)

    i = j = 0
    res = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    res += a[i:]
    res += b[j:]

    return res

def countInversions(A):
    if len(A) < 2:
        return 0

    mid = len(A) // 2
    left_half, right_half = A[:mid], A[mid:]

    left_inversion_count = countInversions(left_half)
    right_inversion_count = countInversions(right_half)

    i = j = k = 0
    inversion_count = 0

    while (i < len(left_half) and j < len(right_half)):
        if (left_half[i] < right_half[j]):
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
