'''
57. Insert Interval
Link: https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
Output: [[1, 5], [6, 9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5, 7]
Output: [[5, 7]]
'''


def insert_interval(intervals, newInterval):
    '''https://www.youtube.com/watch?v=A8NUOmlwOlM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=35'''

    n = len(intervals)
    res = []

    for i in range(n):
        current_interval = intervals[i]
        start, end = newInterval[0], newInterval[1]

        if start > current_interval[1]:
            res.append(current_interval)
        elif end < current_interval[0]:
            res.append(newInterval)
            return res + intervals[i:]  # all other intervals cannot overlap
        else:
            new_start = min(start, current_interval[0])
            new_end = max(end, current_interval[1])
            newInterval = [new_start, new_end]

    res.append(newInterval)
    return res
