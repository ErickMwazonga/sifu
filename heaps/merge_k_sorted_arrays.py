'''
Merge K Sorted Arrays

Input: [[1, 10, 11, 15],
        [2,  4,  9, 14],
        [5,  6,  8, 16],
        [3,  7, 12, 13]]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

Naive Approach
Put k lists in one big list - O(n*k), 
Then sort the big list quicksort. 
Overall time complexity would be O(nk)+O(nk log(nk)) = O(nk log(nk)).

Best Approach
https://medium.com/@amitrajit_bose/merge-k-sorted-arrays-6f9427661e67
https://medium.com/outco/how-to-merge-k-sorted-arrays-c35d87aa298e
'''

import heapq


def merge(lists):
    final_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, row_idx, col_idx = heapq.heappop(heap)
        final_list.append(val)

        if col_idx + 1 < len(lists[row_idx]):
            next_val = lists[row_idx][col_idx + 1]
            next_tuple = (next_val, row_idx, col_idx + 1)
            heapq.heappush(heap, next_tuple)

    return final_list
