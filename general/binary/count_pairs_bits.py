"""
Count pairs in an array such that both elements has equal set bits
Given an array arr with unique elements,
the task is to count the total number of pairs of elements that have equal set bits count.

Examples:
Input: arr[] = {2, 5, 8, 1, 3}
Output: 4
Set bits counts for {2, 5, 8, 1, 3} are {1, 2, 1, 1, 2}
All pairs with same set bits count are {2, 8}, {2, 1}, {5, 3}, {8, 1}

Input: arr[] = {1, 11, 7, 3}
Output: 1
Only possible pair is {11, 7}
"""


def totalPairs(arr):
    n = len(arr)
    m = dict()  # elems_with_same_lengths

    for i in range(n):
        x = bin(arr[i]).count('1')
        m[x] = m.get(x, 0) + 1

    res = 0
    for i in m:
        # there can be (n*(n-1)/2) unique two-
        # element pairs to choose from n elements
        res += (m[i] * (m[i] - 1)) // 2

    return res


arr = [2, 5, 8, 1, 3]
print(totalPairs(arr))
