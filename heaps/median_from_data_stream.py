'''
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
Credit: https://www.youtube.com/watch?v=itmhHWaHupI  

The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input
['MedianFinder', 'addNum', 'addNum', 'findMedian', 'addNum', 'findMedian']
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
'''

import heapq


class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if (self.small and self.large) and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) - len(self.large) > 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2
