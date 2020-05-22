'''
CHALLENGE: COUNTING INVERSIONS
If array is already sorted then inversion count is 0.
If array is sorted in reverse order that inversion count is the maximum.
GENERALLY two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
'''


def countInversions(A):
    if len(A) < 2:
        return 0

    mid = len(A) // 2
    left_half = A[:mid]
    right_half = A[mid:]

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
            # they are greate than current right element
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
