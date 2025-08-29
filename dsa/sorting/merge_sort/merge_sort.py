class MergeSort:

    def mergeSort(self, A):
        '''Time O(n*log n), Space O(n)'''

        if len(A) < 2:
            return A

        mid = len(A) // 2
        left, right = A[:mid], A[mid:]

        self.mergeSort(left)
        self.mergeSort(right)

        self.merge(A, left, right)

    def merge(self, A, left, right):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i, k = i + 1, k + 1

        while j < len(right):
            A[k] = right[j]
            j, k = j + 1, k + 1

    def merge_v2(self, A, left, right):
        i = j = k = 0

        while i < len(left) or j < len(right):
            if i < len(left) and j < len(right):
                if left[i] < right[j]:
                    A[k] = left[i]
                    i += 1
                else:
                    A[k] = right[j]
                    j += 1
            elif i < len(left):
                A[k] = left[i]
                i += 1
            else:
                A[k] = left[j]
                j += 1

            k += 1


soln = MergeSort()
A = [8, 7, 2, 1, 0, 9, 6]
assert soln.mergeSort(A) == list(sorted(A))
