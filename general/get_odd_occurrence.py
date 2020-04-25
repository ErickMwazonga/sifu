"""
https://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
Given an array of positive integers.
All numbers occur even number of times except 
one number which occurs odd number of times.
Find the number in O(n) time & constant space.
Examples :
Input : arr = {1, 2, 3, 2, 3, 1, 3}
Output : 3

Input : arr = {5, 7, 2, 7, 5, 2, 5}
Output : 5
"""

def get_odd_occurrence(arr):
    '''Time complexity: O(n)'''
    
    size = len(arr)
    _hash = dict()

    for i in range(size):
        elem = arr[i]
        _hash[elem] = _hash.get(elem, 0) + 1

    for k, v in _hash.items(): 
        if (v % 2 != 0): return k
    return -1

A = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2] 
assert get_odd_occurrence(A) == 5
assert get_odd_occurrence([1, 2, 3, 2, 3, 1, 3]) == 3
assert get_odd_occurrence([5, 7, 2, 7, 5, 2, 5]) == 5