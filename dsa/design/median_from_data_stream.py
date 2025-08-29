'''
295. Find Median from Data Stream
Link: https://leetcode.com/problems/find-median-from-data-stream/
Resource: https://www.youtube.com/watch?v=itmhHWaHupI  

The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2, 3, 4], the median is 3.
For example, for arr = [2, 3],  the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
1. MedianFinder() initializes the MedianFinder object.
2. void addNum(int num) adds the integer num from the data stream to the data structure.
3. double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input
['MedianFinder', 'addNum', 'addNum', 'findMedian', 'addNum', 'findMedian']
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
'''

from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        self.small = []  # maxHeap,
        self.large = []  # minHeap (python default)

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)

        # every element in small has to lesser than every element in large
        if (self.small and self.large) and (-self.small[0] > self.large[0]):
            val = -heappop(self.small)
            heappush(self.large, val)

        # uneven sizes
        if len(self.small) - len(self.large) > 1:
            popped = -heappop(self.small)
            heappush(self.large, popped)
        if len(self.large) - len(self.small) > 1:
            popped = heappop(self.large)
            heappush(self.small, -popped)

    def findMedian(self) -> float:
        n_small, n_large = len(self.small), len(self.large)

        if n_small > n_large:
            return -self.small[0]

        if n_large > n_small:
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2
