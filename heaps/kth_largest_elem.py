'''
Find the kth largest element in an unsorted array.
https://leetcode.com/problems/kth-largest-element-in-an-array/

Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Examples
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''

import heap as theHeap


def find_Kth_largest(nums, k):
    nums.sort()
    n = len(nums)

    return nums[n - k]


def find_Kth_largest1(nums, k):
    res = sorted(nums, reverse=True)
    return res[k - 1]


def findKthLargest(nums, k):
    '''Time: O(nlogn)'''

    return sorted(nums)[-k]


def findKthLargest2(nums, k):
    '''Time: O(klogn)'''
    import heapq

    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)

    while k > 1:
        heapq.heappop(max_heap)
        k -= 1

    return -max_heap[0]


def findKthLargest_CUSTOM(nums, k):
    heapx = theHeap.MinHeap('MAX')
    max_heap = heapx.build_heap(nums)

    for _ in range(k-1):
        heapx.heappop(max_heap)

    return max_heap[0]


assert findKthLargest([9, 5, 3, 1, 4, 2], 3) == 4
assert findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

assert findKthLargest_CUSTOM([9, 5, 3, 1, 4, 2], 3) == 4
assert findKthLargest_CUSTOM([3, 2, 1, 5, 6, 4], 2) == 5
assert findKthLargest_CUSTOM([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
