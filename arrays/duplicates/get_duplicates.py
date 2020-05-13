"""
Imagine you have a list in memory of length n.
The elements of the list are drawn from the set of integers between [1,n-1].
So, you’re guaranteed to have at least one duplicate in the list.
You have to write a function that prints out a duplicate in the list.

Valid:
    [1,2,1] -> 1
    [3,3,3,3,3,3] -> 3
    [1,2,1,2] -> 1,2

Invalid:
    [1]
    [1,2]
"""


def get_duplicates(arr):
    counts = {}

    if arr == set(arr):
        print('Invalid')

    for value in arr:
        if value in counts:
            counts[value] += 1
            if counts.get(value) == 2: print(value, end=' ')
        else:
            counts[value] = 1


get_duplicates([1, 2, 2, 2, 3])
# get_duplicates([1,2,1,2])
