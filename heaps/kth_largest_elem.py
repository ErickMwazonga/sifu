'''
Find the kth largest element in an unsorted array.
https://leetcode.com/problems/kth-largest-element-in-an-array/

Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Examples
Input: [3, 2, 1, 5, 6, 4] and k = 2
Output: 5

Input: [3, 2, 3, 1, 2, 4, 5, 5, 6] and k = 4
Output: 4
'''

import heap as theHeap


def find_Kth_largest(nums, k):
    n = len(nums)
    nums.sort()

    return nums[n - k]


def find_Kth_largest_v2(nums, k):
    res = sorted(nums, reverse=True)
    return res[k - 1]


def find_Kth_largest_v3(nums, k):
    '''
    Time: O(n + klogn) -> O(klogn)
    k~n => O(nlogn), k~0 => O(logn)
    '''

    import heapq

    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)  # O(n)

    for _ in range(k-1):
        heapq.heappop(max_heap)

    # return -heapq.heappop(nums)
    return -max_heap[0]


def find_Kth_largest_v5(nums, k):
    heapx = theHeap.MinHeap('MAX')
    max_heap = heapx.build_heap(nums)

    for _ in range(k-1):
        heapx.heappop(max_heap)

    return max_heap[0]


assert find_Kth_largest([9, 5, 3, 1, 4, 2], 3) == 4
assert find_Kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
assert find_Kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

assert find_Kth_largest_v2([9, 5, 3, 1, 4, 2], 3) == 4
assert find_Kth_largest_v2([3, 2, 1, 5, 6, 4], 2) == 5
assert find_Kth_largest_v2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
