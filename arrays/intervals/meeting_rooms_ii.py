'''
919 · Meeting Rooms II
https://leetcode.com/problems/meeting-rooms/ OR https://www.lintcode.com/problem/919
Resource: https://www.youtube.com/watch?v=FdzJmTCVyJU&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=38

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.)

NB: (0,8),(8,10) is not conflict at 8

Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2

Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
'''


import heapq


def minMeetingRooms(self, intervals):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res, count = 0, 0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1

        res = max(res, count)

    return res


def minMeetingRooms(self, intervals) -> int:
    meetings = []

    intervals = sorted(intervals, key=lambda x: x[0])
    heapq.heappush(meetings, intervals[0][1])

    for interval in intervals[1:]:
        if interval[0] >= meetings[0]:
            heapq.heappop(meetings)
            heapq.heappush(meetings, interval[1])
        else:
            heapq.heappush(meetings, interval[1])

    return len(meetings)
