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


class QuickSort:
    def swap(self, A, i, j):
        A[i], A[j] = A[j], A[i]

    def partition(self, A, low, high):
        pivot = A[high]
        i = low

        for j in range(low, high):  # Upto the 2nd last element
            if A[j] <= pivot:
                self.swap(A, i, j)
                i += 1

        self.swap(A, i, high)
        return i

    def qs_helper(self, A, low, high):
        if low >= high:
            return

        pi = self.partition(A, low, high)
        self.qs_helper(A, low, pi-1)
        self.qs_helper(A, pi+1, high)

    def quickSort(self, A):
        n = len(data)
        self.qs_helper(A, 0, n-1)


data = [8, 7, 2, 1, 0, 9, 6]
qs = QuickSort()
qs.quickSort(data)

assert data == [0, 1, 2, 6, 7, 8, 9]


class QuickSort_V2:
    def quick_sort(self, A):
        length = len(A)

        if length <= 1:
            return A

        pivot = A.pop()
        items_greater, items_lower = [], []

        for item in A:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

        return self.quick_sort(items_lower) + [pivot] + self.quick_sort(items_greater)
