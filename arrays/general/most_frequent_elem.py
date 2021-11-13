'''
Find the most frequent element in an array

Problem Description: Given an array A[] of size n, find the most frequent element in the array, 
i.e. the element which occurs the most number of times. 
It is assured that at least one element is repeated.

For example:
Input: A[] = [3, 9, 1, 3, 6, 3, 8, 1, 6]
Output: 3

Input: A[] = [1, 9, 1, 3, 2, 3, 10]
Output: 1
'''


def most_freq_elem(arr):
    mapping = {}

    for num in arr:
        mapping[num] = mapping.get(num, 0) + 1

    most_frequent, most_count = -1, 0

    for key, val in mapping.items():
        if val > most_count:
            most_count = val
            most_frequent = key

    return most_frequent


def most_freq_elem2(arr):
    mapping = {}
    most_frequent, most_count = -1, 0

    for num in arr:
        mapping[num] = mapping.get(num, 0) + 1

        if mapping[num] > most_count:
            most_count = mapping[num]
            most_frequent = num

    return most_frequent


def most_freq_elem3(arr):
    mapping = {}

    for num in arr:
        mapping[num] = mapping.get(num, 0) + 1

    return max(mapping, key=mapping.get)


# TESTING
assertions = [
    {'input': [3, 9, 1, 3, 6, 3, 8, 1, 6], 'output': 3},
    {'input': [1, 9, 1, 3, 2, 3, 10], 'output': 1}
]

for assertion in assertions:
    _input, output = assertion['input'], assertion['output']

    assert most_freq_elem(_input) == output
    assert most_freq_elem2(_input) == output
    assert most_freq_elem3(_input) == output
