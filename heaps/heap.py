class Heap:
    '''Min Heap Implementaion'''

    def parent(self, pos):
        return (pos - 1) // 2

    def left(self, pos):
        return (2 * pos) + 1

    def right(self, pos):
        return (2 * pos) + 2

    def isLeaf(self, A, pos):
        n = len(A)
        return pos <= n and pos >= (n // 2)

    def heapify(self, A, pos):
        '''O(log(n))'''

        n = len(A)
        left, right = self.left(pos), self.right(pos)

        smallest = pos
        if left < n and A[left] < A[pos]:
            smallest = left

        if right < n and A[right] < A[smallest]:
            smallest = right

        if smallest != pos:
            A[pos], A[smallest] = A[smallest], A[pos]
            self.heapify(A, smallest)

    def maxHeapify(self, A, pos):
        n = len(A)
        left, right = self.left(pos), self.right(pos)

        largest = pos
        if left < n and A[left] > A[pos]:
            largest = left

        if right < n and A[right] > A[largest]:
            largest = right

        if largest != pos:
            A[pos], A[largest] = A[largest], A[pos]
            self.heapify(A, largest)

    def build_min_heap(self, A):
        ''' O(nlog(n)) '''

        n = len(A)
        no_leaf_nodes_max_idx = (n // 2) - 1

        for k in range(no_leaf_nodes_max_idx, -1, -1):
            self.heapify(A, k)

        return A

    def build_heap(self, A, type='MIN'):
        n = len(A)
        no_leaf_nodes_max_idx = (n // 2) - 1

        is_min = type == 'MIN'
        for k in range(no_leaf_nodes_max_idx, -1, -1):
            self.heapify(A, k) if is_min else self.maxHeapify(A, k)

        return A

    def heappush(self, A, val):
        A.append(val)
        self.build_heap(A)

    def heappop(self, A):  # Extract Min val
        n = len(A)

        # Swap first and last element
        A[0], A[n-1] = A[n-1], A[0]
        popped = A.pop()

        self.build_heap(A)
        return popped


A = [3, 9, 2, 1, 4, 5]
heapq = Heap()
assert heapq.build_heap(A) == [1, 3, 2, 9, 4, 5]
