'''
1109. Corporate Flight Bookings
https://leetcode.com/problems/corporate-flight-bookings/description/

There are n flights that are labeled from 1 to n.
You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi]
represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

Example 1:
Input: bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]],  n = 5
Output: [10, 55, 45, 25, 25]
Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence,  answer = [10, 55, 45, 25, 25]

INTUITION:
We can use a difference array approach to efficiently calculate the total number of seats reserved for each flight.
'''

def corpFlightBookings(bookings: list[list[int]], n: int) -> list[int]:
    result = [0] * n
    
    for first, last, seats in bookings:
        result[first - 1] += seats
        if last < n:
            result[last] -= seats
    
    # Prefix sum to accumulate bookings
    for i in range(1, n):
        result[i] += result[i - 1]
    
    return result