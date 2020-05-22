def mergeSort(A):
    '''
    Time O(n*log n), Space O(n)
    '''

    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

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


# ABSTRACT SOLUTION - TO BE REVISED
def mergeSort2(A, low, high):
    if low < high:
        mid = (high + low) // 2
        mergeSort2(A, low, mid)
        mergeSort2(A, mid+1, high)
        merge(A, low, mid, high)


def merge(A, low, mid, high):
    len_lefthalf = (mid - low) + 1
    len_righthalf = high - mid

    # create temp arrays
    L = [0] * len_lefthalf
    R = [0] * len_righthalf

    # Copy data to temp arrays L[] and R[]
    for i in range(0, len_lefthalf):
        L[i] = A[low + i]

    for j in range(0, len_righthalf):
        R[j] = A[mid + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = low     # Initial index of merged subarray

    while i < len_lefthalf and j < len_righthalf:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements of L[]
    while i < len_lefthalf:
        A[k] = L[i]
        i += 1
        k += 1

    # Copy any remaining elements of R[]
    while j < len_righthalf:
        A[k] = R[j]
        j += 1
        k += 1


A = [8, 7, 2, 1, 0, 9, 6]
size = len(A)
# mergeSort(A, 0, size - 1)


mergeSort(A)
assert A == [0, 1, 2, 6, 7, 8, 9]
