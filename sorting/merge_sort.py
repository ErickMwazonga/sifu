def mergeSort(A):
    '''Time O(n*log n), Space O(n)'''

    n = len(A)

    if n < 2:
        return A

    mid = n // 2
    L, R = A[:mid], A[mid:]

    # Sort the two halves
    mergeSort(L)
    mergeSort(R)

    i = j = k = 0

    # Until we reach either end of either L or M
    # pick smaller among them
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


A = [8, 7, 2, 1, 0, 9, 6]

mergeSort(A)
assert A == [0, 1, 2, 6, 7, 8, 9]


def mergeSortV2(A):
    n = len(A)

    if n < 2:
        return

    mid = n // 2
    L, R = A[:mid], A[mid:]

    mergeSort(L)
    mergeSort(R)

    i = j = k = 0

    while i < len(L) or j < len(R):
        if i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        elif i < len(L):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

        k += 1
