'''
919 · Meeting Rooms II
Link: https://leetcode.com/problems/meeting-rooms/ OR https://www.lintcode.com/problem/919
Resource: https://www.youtube.com/watch?v=FdzJmTCVyJU&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=38

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.)

NB: (0, 8), (8, 10) is not conflict at 8

Example1
Input: intervals = [(0, 30), (5, 10), (15, 20)]
Output: 2

Explanation:
We need two meeting rooms
room1: (0, 30)
room2: (5, 10), (15, 20)
'''


import heapq


def minimum_rooms(intervals):
    starting_times = sorted([i[0] for i in intervals])
    ending_times = sorted([i[1] for i in intervals])

    rooms = 0
    while starting_times:
        startTime = starting_times.pop(0)
        # now a meeting is going to start, is there a meeting ends
        # (meaning a meeting room is released)?
        endTime = ending_times[0]

        if endTime <= startTime:
            ending_times.pop(0)
        else:
            # need to ask for a new room
            rooms += 1

    return rooms


def minimum_rooms_v2(intervals):
    '''
    Inspired by
    https://medium.com/javascript-in-plain-english/snapchat-coding-interview-questions-377fc67e0cbe
    '''

    starting_times, ending_times = [], []

    starting_times = sorted([i[0] for i in intervals])
    ending_times = sorted([i[1] for i in intervals])

    starting_index = ending_index = 0
    max_rooms = current_rooms = 0

    while starting_index < len(starting_times) and ending_index < len(ending_times):
        if starting_index >= len(starting_times):
            break

        if starting_times[starting_index] < ending_times[ending_index]:
            current_rooms += 1
            starting_index += 1
        else:
            current_rooms -= 1
            ending_index += 1

        max_rooms = max(max_rooms, current_rooms)

    return max_rooms


def minMeetingRooms_v2(intervals) -> int:
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


def minimum_rooms(intervals):
    starting_times = sorted([i[0] for i in intervals])
    ending_times = sorted([i[1] for i in intervals])

    rooms = 0
    while starting_times:
        startTime = starting_times.pop(0)
        # now a meeting is going to start, is there a meeting ends
        # (meaning a meeting room is released)?
        endTime = ending_times[0]

        if endTime <= startTime:
            ending_times.pop(0)
        else:
            # need to ask for a new room
            rooms += 1

    return rooms


def minimum_rooms_v2(intervals):
    '''
    Inspired by
    https://medium.com/javascript-in-plain-english/snapchat-coding-interview-questions-377fc67e0cbe
    '''

    starting_times, ending_times = [], []

    starting_times = sorted([i[0] for i in intervals])
    ending_times = sorted([i[1] for i in intervals])

    starting_index = ending_index = 0
    max_rooms = current_rooms = 0

    while starting_index < len(starting_times) and ending_index < len(ending_times):
        if starting_index >= len(starting_times):
            break

        if starting_times[starting_index] < ending_times[ending_index]:
            current_rooms += 1
            starting_index += 1
        else:
            current_rooms -= 1
            ending_index += 1

        max_rooms = max(max_rooms, current_rooms)

    return max_rooms


intervals = [[30, 75], [0, 50], [60, 150]]
assert minimum_rooms(intervals) == 2

intervals = [[5, 7], [0, 9], [5, 9]]
assert minimum_rooms(intervals) == 3
