'''
729. My Calendar I
https://leetcode.com/problems/my-calendar-i/

Implement a MyCalendar class to store your events.
A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally,
this represents a booking on the half open interval [start, end),
the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty
intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can
be added to the calendar successfully without causing a double booking.
Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
 
Note:
The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
'''

# Approach #1: Brute Force [Accepted]
class MyCalendar:
    '''
    Time Complexity: O(N^2) where N is the number of events booked. For each new event,
    we process every previous event to decide whether the new event can be booked.
    Space Complexity: O(N)O(N), the size of the calendar.
    '''

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if s < end and start < e:
                return False

        self.calendar.append((start, end))
        return True


# Approach #2: Balanced Tree [Accepted]
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
    
    def insert(self, node):
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            else:
                return self.left.insert(node)
        elif node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            else:
                return self.right.insert(node)
        else:
            return False
        
        
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        node = Node(start, end)
        
        if not self.root:
            self.root = node
            return True
        
        return self.root.insert(node)
