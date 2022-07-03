'''
Find the most frequent element in an array

Problem Description: Given an array A[] of size n, find the most frequent element in the array, 
i.e. the element which occurs the most number of times. 
It is assured that at least one element is repeated.

Examplea:
1. [3, 9, 1, 3, 6, 3, 8, 1, 6] -> 3
2. [1, 9, 1, 3, 2, 3, 10] -> 1
'''


def most_freq_elem(arr):
    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    most_frequent, most_count = -1, 0

    for key, val in frequency.items():
        if val > most_count:
            most_count = val
            most_frequent = key

    return most_frequent


def most_freq_elem_v2(arr):
    frequency = {}
    most_frequent, most_count = -1, 0

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

        curr_count = frequency[num]
        if curr_count > most_count:
            most_count = curr_count
            most_frequent = num

    return most_frequent


def most_freq_elem_v3(arr):
    freqs = {}

    for num in arr:
        freqs[num] = freqs.get(num, 0) + 1

    return max(freqs, key=freqs.get)


# TESTING
assertions = [
    {'input': [3, 9, 1, 3, 6, 3, 8, 1, 6], 'output': 3},
    {'input': [1, 9, 1, 3, 2, 3, 10], 'output': 1},
    {'input': [10, 20, 10, 20, 30, 20, 20], 'output': 20}
]

for assertion in assertions:
    _input, output = assertion['input'], assertion['output']

    assert most_freq_elem(_input) == output
    assert most_freq_elem_v2(_input) == output
    assert most_freq_elem_v3(_input) == output
