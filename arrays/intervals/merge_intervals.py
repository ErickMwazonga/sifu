'''
56. Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Explanation: Since intervals [1, 3] and [2, 6] overlaps,  merge them into [1, 6].

Example 2:
Input: intervals = [[1, 4], [4, 5]]
Output: [[1, 5]]
'''


def merge(intervals):
    intervals.sort(key=lambda pair: pair[0])
    res = [intervals[0]]

    for interval in intervals[1:]:
        start, end = interval
        last_end = res[-1][1]

        if start > last_end:
            res.append(interval)
        else:
            res[-1][1] = max(last_end, end)

    return res


def merge_ranges(meetings):
    '''O(nlogn) time and O(n) space.'''

    sorted_meetings = sorted(meetings)  # Sort by start time
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        if (current_meeting_start > last_merged_meeting_end):
            # Add the current meeting since it doesn't overlap
            merged_meetings.append(
                (current_meeting_start, current_meeting_end))
        else:
            # If the current meeting overlaps with the last merged meeting, use the
            # later end time of the two
            new_meeting_end = max(last_merged_meeting_end, current_meeting_end)
            merged_meetings[-1] = (last_merged_meeting_start, new_meeting_end)

    return merged_meetings


meetings1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
assert merge_ranges(meetings1) == [(0, 1), (3, 8), (9, 12)]

meetings2 = [(1, 3), (5, 8), (4, 10), (20, 25)]
assert merge_ranges(meetings2) == [(1, 3), (4, 10), (20, 25)]


intervals = [[1, 4], [5, 8], [7, 10], [9, 13], [14, 16], [16, 20], [17, 19]]
assert merge(intervals) == [[1, 4], [5, 13], [14, 20]]
