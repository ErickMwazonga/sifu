class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


'''
# BUBBLESORT 
Time complexity: O(n²)
Space complexity: O(1)
'''


def sortArray(list):
    i = list.head

    while i:
        j = list.head

        while j:
            if j.data > j.next.data:
                j.data, j.next.data = j.next.data, j.data
            j = j.next

        i = i.next


def sortArray_v2(A):
    i = 0

    while i < len(A):
        j = 0

        while j + 1 < len(A):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            j += 1
        i += 1
