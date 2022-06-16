'''
920· Meeting Rooms
Link: https://leetcode.com/problems/meeting-rooms/ OR https://www.lintcode.com/problem/920/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

(0, 8), (8, 10) is not conflict at 8

Example1
Input: intervals = [(0, 30), (5, 10), (15, 20)]
Output: false
Explanation: 
(0, 30), (5, 10) and (0, 30), (15, 20) will conflict

Example2
Input: intervals = [(5, 8), (9, 15)]
Output: true
'''


def canAttendMeetings(intervals):
    if not intervals:
        return True

    intervals.sort(key=lambda x: x.start)

    for i, interval in enumerate(intervals[1:]):
        prev = intervals[i-1]

        if prev.end > interval.start:
            return False

    return True


def canAttendMeetings_v2(intervals):
    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]

        if i1.end > i2.start:
            return False

    return True
