import heapq


class Solution:
    '''O(nlogn)'''
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]


class Solution1:
    def findKthLargest(self, nums, k):
        q = []

        # Min heap
        for i in range(len(nums)):
            heapq.heappush(q, nums[i])
            if len(q) > k:
                heapq.heappop(q)

        # First one is kth largest
        return heapq.heappop(q)


# BEST SOLUTION
class KthLargestElement:
    '''Max-heap O(klogn) time, O(n+k) space'''
    '''Min-heap O(n-k+1logn-k+1) time, O(n-k+1) space'''

    def min_heapify(self, array, i):
        # O(logn) time
        smallest = i

        left = 2 * i + 1
        right = 2 * i + 2
        last_elem = len(array) - 1

        if left <= last_elem and array[left] < array[smallest]:
            smallest = left

        if right <= last_elem and array[right] < array[smallest]:
            smallest = right

        # swap if not smallest
        if smallest != i:
            array[smallest], array[i] = array[i], array[smallest]
            self.max_heapify(array, smallest)

    def max_heapify(self, array, i):
        # O(logn) time
        largest = i

        left = 2 * i + 1
        right = 2 * i + 2
        last_elem = len(array) - 1

        if left <= last_elem and array[left] > array[largest]:
            largest = left

        if right <= last_elem and array[right] > array[largest]:
            largest = right

        # swap if not smallest
        if largest != i:
            array[largest], array[i] = array[i], array[largest]
            self.max_heapify(array, largest)

    def build_max_heap(self, A):
        # O(n) time
        size = len(A)
        no_leaf_nodes_max_idx = (size // 2) - 1
        for i in range(no_leaf_nodes_max_idx, -1, -1):
            self.max_heapify(A, i)

    def heapsort(self, array, times):
        sorted_array = []

        # build a heap from the array
        self.build_max_heap(array)

        # the biggest element is always at the end i.e. one of the leaves
        # pop the last most leaf and append to the sorted array
        # then maxify heap
        # iterate for length of array to sort entire array
        for _ in range(times):
            array[0], array[-1] = array[-1], array[0]
            sorted_array.append(array.pop())

            # heapify remaining
            self.max_heapify(array, 0)

        return sorted_array[-1]


kle = KthLargestElement()
assert kle.heapsort([9, 5, 3, 1, 4, 2], 3) == 4


# REVISIT
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        heap=[]
        for i in range(k):
            b=heapq.heappop(nums)
            heapq.heappush(heap,b)
        while nums:
            c=heapq.heappop(nums)
            while len(heap) >= k:
                heapq.heappop(heap)
            heapq.heappush(heap,c)
        d=heapq.heappop(heap)
        return d