'''
435. Non-overlapping Intervals
Link: https://leetcode.com/problems/non-overlapping-intervals/
Resource: https://www.youtube.com/watch?v=nONCGxWoUfM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=36

Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: [1, 3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1, 2], [1, 2], [1, 2]]
Output: 2
Explanation: You need to remove two [1, 2] to make the rest of the intervals non-overlapping
'''


def eraseOverlapIntervals(intervals):
    intervals.sort()

    count = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= prev_end:  # Not overlapping
            prev_end = end
        else:  # Overlapping
            count += 1
            prev_end = min(end, prev_end)

    return count
