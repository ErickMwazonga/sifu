class MaxHeap:
    '''
    A Max-Heap is a complete binary tree in which the value in each internal
    node is greater than or equal to the values in the children of that node.
    '''

    def parent(self, pos):
        return (pos - 1) // 2

    def leftChild(self, pos):
        return (2 * pos) + 1

    def rightChild(self, pos):
        return (2 * pos) + 2

    def isLeaf(self, A, pos):
        n = len(A)
        return pos <= n and pos >= (n // 2)

    def maxHeapify(self, A, n, i):
        largest = i
        left_child = self.leftChild(i)
        right_child = self.rightChild(i)

        if left_child < n and A[left_child] > A[i]:
            largest = left_child

        if right_child < n and A[right_child] > A[largest]:
            largest = right_child

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.maxHeapify(A, n, largest)   # Heapify the sub heap

    def build_max_heap(self, A):
        # O(n) time
        n = len(A)
        no_leaf_nodes_max_idx = (n // 2) - 1

        for i in range(no_leaf_nodes_max_idx, -1, -1):
            self.maxHeapify(A, n, i)

    def insertNode(self, A, num):
        '''Time - Heapify optimizes from O(nlogn) to O(n)'''

        n = len(A)
        if not n:
            A.append(num)
        else:
            A.append(num)
            self.build_max_heap(A)

    def deleteNode(self, A):  # extractMax
        '''Time - Heapify optimizes from O(nlogn) to O(n)'''

        n = len(A)

        # Swap first and last element
        A[0], A[n-1] = A[n-1], A[0]

        popped = A.pop()

        self.build_max_heap(A)

        return popped

    def heapSort(self, A):
        '''Time - Heapify optimizes from O(nlogn) to O(n)'''

        self.build_max_heap(A)

        # Heapify root element iteratively
        for i in range(n-1, 0, -1):
            # Swap elements
            A[i], A[0] = A[0], A[i]
            self.maxHeapify(A, i, 0)

    def kthLargestHeapsort(self, A, times):
        self.build_max_heap(A)

        # One by one extract elements
        sorted_array = []
        for i in range(times):
            A[-1], A[0] = A[0], A[-1]
            sorted_array.append(A.pop())
            self.maxHeapify(A, i, 0)

        return sorted_array[-1]


# -------------------------------
mh = MaxHeap()

arr = [3, 12, 11, 13, 5, 6, 7]
sorted_arr = sorted(arr)
mh.heapSort(arr)
assert arr == sorted_arr

# -------------------------------

A = []
mh.insertNode(A, 3)
mh.insertNode(A, 1)
mh.insertNode(A, 4)
mh.insertNode(A, 9)
mh.insertNode(A, 5)
mh.insertNode(A, 2)

assert A == [9, 5, 3, 1, 4, 2]

# -------------------------------

assert mh.deleteNode(A) == 9
assert A == [5, 4, 3, 1, 2]
