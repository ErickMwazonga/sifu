'''
CHALLENGE: COUNTING INVERSIONS
If array is already sorted then inversion count is 0.
If array is sorted in reverse order that inversion count is the maximum.
GENERALLY two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
'''


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



class CountInversions:

    def countInversions(self, A):
        n = len(A)

        if n < 2:
            return 0

        mid = n // 2
        left_half, right_half = A[:mid], A[mid:]

        left_inversion_count = self.countInversions(left_half)
        right_inversion_count = self.countInversions(right_half)

        inversion_count = self.merge_and_count_inversions(A, left_half, right_half)

        return inversion_count + left_inversion_count + right_inversion_count


    def merge_and_count_inversions(self, A, left_half, right_half):
        i = j = k = 0
        inversion_count = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
                inversion_count += len(left_half) - i
            k += 1

        while i < len(left_half):
            A[k] = left_half[i]
            i, k = i + 1, k + 1

        while j < len(right_half):
            A[k] = right_half[j]
            j, k = j + 1, k + 1

        return inversion_count

    def countInversions_v2(self, A):
        n = len(A)

        if n < 2:
            return 0

        mid = n // 2
        left_half, right_half = A[:mid], A[mid:]

        left_inversion_count = self.countInversions_v2(left_half)
        right_inversion_count = self.countInversions_v2(right_half)

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
            i, k = i + 1, k + 1

        while j < len(right_half):
            A[k] = right_half[j]
            j, k = j + 1, k + 1

        return inversion_count + left_inversion_count + right_inversion_count


soln = CountInversions()
assert soln.countInversions([2, 4, 3, 1, 5]) == 4
assert soln.countInversions([1, 20, 6, 4, 5]) == 5
