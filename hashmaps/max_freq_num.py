'''
You are given an array of integers that contain numbers in random order.
Example: The most frequently occurring item in [1, 3, 1, 3, 2, 1] is 1.
Write a program to find and return the number which occurs
the maximum times in the given input.
If two or more elements contend for the maximum frequency,
return any of the elements.
'''


def mostFrequent(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    max_count, res = 0, -1
    for k, v in freq.items():
        if v > max_count:
            max_count = v
            res = k

    return res


def mostFrequent2(arr):
    freq = {}
    max_count, most_frequent = 0, -1

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

        curr = freq[num]
        if curr > max_count:
            max_count = curr
            most_frequent = num

    return most_frequent


A = [1, 5, 2, 1, 3, 2, 1]
assert mostFrequent(A) == 1
assert mostFrequent2(A) == 1
