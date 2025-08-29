import heap as theHeap


def heap_sort(A):
    heapq = theHeap.Heap()

    # heap = []
    # for elem in A:
    #     heapq.heappush(heap, elem)

    heap = heapq.build_heap(A)

    ordered = []
    while heap:
        largest = heapq.heappop(heap)
        ordered.append(largest)

    return ordered


A = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
assert(heap_sort(A) == [2, 4, 5, 13, 15, 17, 18, 21, 24, 26])
