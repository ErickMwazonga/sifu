'''
1094. Car Pooling
https://leetcode.com/problems/car-pooling/description/

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] 
indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively.
The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:
Input: trips = [[2, 1, 5], [3, 3, 7]],  capacity = 4
Output: false

Example 2:
Input: trips = [[2, 1, 5], [3, 3, 7]], capacity = 5
Output: true
'''

def carPooling(trips: list[list[int]], capacity: int) -> bool:
    max_location = max(trip[2] for trip in trips)
    diff = [0] * (max_location + 1)

    for num_passengers, start, end in trips:
        diff[start] += num_passengers
        diff[end] -= num_passengers

    current_passengers = 0
    for passengers in diff:
        current_passengers += passengers
        if current_passengers > capacity:
            return False

    return True


def carPooling2(trips: list[list[int]], capacity: int) -> bool:
    max_location = max(trips, key=lambda x: x[2])[2]
    diff = [0] * max_location

    for num_passengers, start, end in trips:
        diff[start] += num_passengers
        if end < max_location:
            diff[end] -= num_passengers

    for i in range(1, max_location):
        diff[i] += diff[i - 1]
        if diff[i] > capacity:
            return False

    # Check the first element separately, since prefix sum starts from i=1
    return diff[0] <= capacity
