'''
75. Sort Colors
https://leetcode.com/problems/sort-colors/

For this problem, your goal is to sort an array of 0, 1 and 2's
but you must do this in place, in linear time and without 
any extra space (such as creating an extra array).
This is called the Dutch national flag sorting problem.

For example, if the input array is [2,0,0,1,2,1] then
your program should output [0,0,1,1,2,2] and the algorithm
should run in O(n) time.
'''


def dutchNationalFlagSorting(A):
    '''Time Complexity: O(n), when n is lenth of array'''

    low, traverse, high = 0, 0, len(A) - 1

    while traverse <= high:
        traverse_value = A[traverse]

        if traverse_value == 0:
            A[low], A[traverse] = A[traverse], A[low]
            low += 1
            traverse += 1
        elif traverse_value == 1:
            traverse += 1
        else:
            A[traverse], A[high] = A[high], A[traverse]
            high -= 1
    return A


first_A = [2, 0, 0, 1, 2, 1]
sec_A = [0, 1, 2, 0, 1, 2]

assert dutchNationalFlagSorting(first_A) == sorted(first_A)
assert dutchNationalFlagSorting(sec_A) == sorted(sec_A)
