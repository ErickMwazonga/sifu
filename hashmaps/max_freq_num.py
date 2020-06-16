'''
You are given an array of integers that contain numbers in random order.
Write a program to find and return the number which occurs
the maximum times in the given input.
If two or more elements contend for the maximum frequency,
return any of the elements.
'''


def mostFrequent(arr):
    '''
    Time Complexity : O(n)
    Auxiliary Space : O(n)
    '''

    n = len(arr)

    # Insert all elements in Hash.
    Hash = {}
    for i in range(n):
        curr_elem = arr[i]
        Hash[curr_elem] = Hash.get(curr_elem, 0) + 1

    # find the max frequency
    max_count = 0
    res = -1
    for i in Hash:
        if (max_count < Hash[i]):
            res = i
            max_count = Hash[i]

    return res


# Driver Code
arr = [1, 5, 2, 1, 3, 2, 1]
print(mostFrequent(arr)