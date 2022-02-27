'''
Imagine you have a list in memory of length n.
The elements of the list are drawn from the set of integers between [1,n-1].
So, you're guaranteed to have at least one duplicate in the list.
You have to write a function that prints out a duplicate in the list.

Valid:
    1. [1,2,1] -> 1
    2. [3,3,3,3,3,3] -> 3
    3. [1,2,1,2] -> 1,2

Invalid:
    [1], [1,2]
'''


def get_duplicates(arr):
    if arr == set(arr):
        return None

    counts, res = {}, []
    for value in arr:
        if value in counts:
            counts[value] += 1

            if counts[value] == 2:
                res.append(value)
        else:
            counts[value] = 1


get_duplicates([1, 2, 2, 2, 3])
# get_duplicates([1,2,1,2])


def findDuplicate2(nums):
    seen, res = set(), set()

    for num in nums:
        if num in seen:
            res.add(num)
        seen.add(num)

    return list(res)
