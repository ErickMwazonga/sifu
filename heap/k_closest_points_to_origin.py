'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
'''

import heapq


def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
    '''# KLOGN'''

    minHeap = []
    res = []

    for point in points:
        x, y = point
        dist = (x ** 2) + (y ** 2)
        minHeap.append([dist, point])

    heapq.heapify(minHeap)

    while k > 0:
        _, point = heapq.heappop(minHeap)
        res.append(point)
        k -= 1

    return res


# NLOGN
def kClosest2(self, points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    res = []

    for point in points:
        x, y = point
        distance = (x ** 2) + (y ** 2)
        heapq.heappush(heap, [distance, point])

    for i in range(k):
        distance, point = heapq.heappop(heap)
        res.append(point)

    return res
