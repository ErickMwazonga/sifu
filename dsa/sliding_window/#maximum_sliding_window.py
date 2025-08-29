'''
239. Sliding Window Maximum
Link: https://leetcode.com/problems/sliding-window-maximum/
Resource: https://www.youtube.com/watch?v=DfljaUwZsOk&t=16s

You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''

import heapq
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        bigger = deque()

        for i, n in enumerate(nums):
            # make sure the rightmost one is the smallest
            while bigger and nums[bigger[-1]] <= n:
                bigger.pop()

            # add in
            bigger += [i]

            # make sure the leftmost one is in-bound
            if i - bigger[0] >= k:
                bigger.popleft()

            # if i + 1 < k, then we are initializing the bigger array
            if i + 1 >= k:
                res.append(nums[bigger[0]])
        return res


class Solution_V2:
    def get_max_in_slinding_window(nums: list[int], K: int) -> list[int]:
        res = []
        heap = []

        n: int = len(nums) - K

        for i in range(n + 1):  # N
            for j in range(i, i + K):  # K
                heapq.heappush(nums[j])  # logK

            res.append(heap[0])
            heap = []

        return res
