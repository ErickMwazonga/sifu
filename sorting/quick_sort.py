'''
https://www.programiz.com/dsa/quick-sort

Worst Case Complexity -> O(n^2)
Pivot element picked is either the greatest or the smallest element.

Best Case Complexity -> O(nlog n)
Pivot element is always the middle element or near to the middle element.

Average Case Complexity [Big-theta]: O(nlog n)
It occurs when the above conditions do not occur.

The space complexity -> O(log n).
'''


def partition(A, low, high):
    pivot = A[high]
    i = low

    for j in range(low, high):  # Upto the 2nd last element
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[high] = A[high], A[i]
    return i


def quickSort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quickSort(A, low, pi-1)
        quickSort(A, pi+1, high)


data = [8, 7, 2, 1, 0, 9, 6]
size = len(data)
quickSort(data, 0, size - 1)

assert data == [0, 1, 2, 6, 7, 8, 9]
