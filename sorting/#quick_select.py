from random import randint


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(A, left, right, pIndex):
    '''Partition using Lomuto partition scheme'''

    pivot = A[pIndex]  # Pick pIndex as pivot from the list
    swap(A, pIndex, right)  # Move pivot to end

    # elements less than pivot will be pushed to the left of pIndex
    # elements more than pivot will be pushed to the right of pIndex
    # equal elements can go either way
    pIndex = left

    # each time we finds an element less than or equal to pivot, pIndex
    # is incremented and that element would be placed before the pivot.
    for i in range(left, right):
        if A[i] <= pivot:
            swap(A, i, pIndex)
            pIndex = pIndex + 1

    swap(A, pIndex, right)  # Move pivot to its place

    return pIndex  # return pIndex (index of pivot element)


# Returns the k-th smallest element of list within left..right
# (i.e. left <= k <= right). The search space within the list is
# changing for each round - but the list is still the same size.
# Thus, k does not need to be updated with each round.
def quickSelect(A, left, right, k):
    # If the list contains only one element, return that element
    if left == right:
        return A[left]

    pIndex = randint(left, right)  # select a pIndex between left and right
    pIndex = partition(A, left, right, pIndex)

    if k == pIndex:  # The pivot is in its sorted position
        return A[k]
    elif k < pIndex:  # if k is less than the pivot index
        return quickSelect(A, left, pIndex - 1, k)
    else:  # if k is more than the pivot index
        return quickSelect(A, pIndex + 1, right, k)


A = [7, 4, 6, 3, 9, 1]
k = 2

print("K'th smallest element is", quickSelect(A, 0, len(A) - 1, k))
