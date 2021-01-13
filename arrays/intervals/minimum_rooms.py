'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

NOTE
- When a new meeting starts, we need an additional room.
- When a meeting ends, we don’t need that room anymore prioritize the smaller starting or
  ending time if the start time and end time are equal, end time comes first.
'''

def minMeetingRooms(self, intervals):
    '''
    Inspired by
    https://medium.com/@edward.zhou/leetcode-253-meeting-rooms-ii-explained-python3-solution-3f8869612df
    '''

    starting_times = [i[0] for i in intervals]
    ending_times = [i[1] for i in intervals]

    starting_times = sorted(starting_times)
    ending_times = sorted(ending_times)

    rooms = 0
    while(len(starting_times) > 0):
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


def minimum_rooms(intervals):
    '''
    Inspired by
    https://medium.com/javascript-in-plain-english/snapchat-coding-interview-questions-377fc67e0cbe
    '''

    starting_times, ending_times = [], []

    starting_times = [i[0] for i in intervals]
    ending_times = [i[1] for i in intervals]

    starting_times.sort()
    ending_times.sort()

    starting_index = ending_index =  0
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


intervals = [(30, 75), (0, 50), (60, 150)]
assert minimum_rooms(intervals) == 2

intervals = [(5, 7), (0, 9), (5, 9)]
assert minimum_rooms(intervals) == 3
