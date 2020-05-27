'''
For example, given:
  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
  [(0, 1), (3, 8), (9, 12)]
'''


def merge_ranges(meetings):
    '''O(nlgn) time and O(n)O(n) space.'''

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            new_meeting_end = max(last_merged_meeting_end, current_meeting_end)
            merged_meetings[-1] = (last_merged_meeting_start, new_meeting_end)
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings


meetings1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
assert merge_ranges(meetings1) == [(0, 1), (3, 8), (9, 12)]

meetings2 = [(1, 3), (5, 8), (4, 10), (20, 25)]
assert merge_ranges(meetings2) == [(1, 3), (4, 10), (20, 25)]
