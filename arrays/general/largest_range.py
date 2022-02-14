'''
Largest Range
Write a function that takes in an array of integers and returns an array of length 2
representing the largest range of integers contained in that array.

The first number in the output array should be the first number in the range,
while the second number should be the last number in the range.
A range of numbers is defined as a set of numbers that come right after each other in the set of real integers.

For instance, the output
array [2, 6] represents the range {2, 3, 4, 5, 6} , which is a range of length 5.
Note that numbers don't need to be sorted or adjacent in the input array in order to form a range.
You can assume that there will only be one largest range.

Example
[1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6] -> [0, 7]

Time complexity: O(n) one pass for creating a hashmap, another pass for traversing each value in the array
Space complexity: O(n) store the hashmap
'''


def largest_range(arr):
    best_range = []
    longest_length = 0
    values_set = {num: True for num in arr}

    for num in arr:
        if not values_set[num]:
            continue

        values_set[num] = False
        current_length = 1
        left, right = num - 1, num + 1

        while left in values_set:
            values_set[left] = False
            current_length += 1
            left -= 1

        while right in values_set:
            values_set[right] = False
            current_length += 1
            right += 1

        if current_length > longest_length:
            longest_length = current_length
            best_range = [left + 1, right - 1]

    return best_range


assert largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]) == [0, 7]
