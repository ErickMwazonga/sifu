'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3], [-2,2]], k = 1
Output: [[-2,2]]

Example 2:
Input: points = [[3,3], [5,-1], [-2,4]], k = 2
Output: [[3,3], [-2,4]]
Explanation: The answer [[-2,4], [3,3]] would also be accepted.
'''

import heapq
import heap as theHeap


def kClosest(points, k):
    '''# KLOGN'''

    heap, res = [], []

    for point in points:
        x, y = point
        dist = (x ** 2) + (y ** 2)
        heapq.heappush(heap, [dist, point])

    for _ in range(k):
        distance, point = heapq.heappop(heap)
        res.append(point)

    return res


def kClosest_CUSTOM(points, k):
    '''# KLOGN'''

    heapqq = theHeap.MinHeap()
    heap, res = [], []

    for point in points:
        x, y = point
        dist = (x ** 2) + (y ** 2)
        heapqq.heappush(heap, [dist, point])

    for _ in range(k):
        distance, point = heapqq.heappop(heap)
        res.append(point)

    return res


assert kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
assert kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]

assert kClosest_CUSTOM([[1, 3], [-2, 2]], 1) == [[-2, 2]]
assert kClosest_CUSTOM([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
