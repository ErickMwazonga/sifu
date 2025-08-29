'''
Common elements in 2 sorted arrays

Design an algorithm to find all the common elements in two sorted lists of numbers. 
For example, for the lists 
A - [1, 1, 2, 3, 5, 5]
B - [2, 2, 3, 4, 5, 7]
output - [2, 3, 5]
'''


def get_common_elements(A, B):
    len_A, len_B = len(A), len(B)

    ai, bi = 0, 0
    result = []

    while ai < len_A and bi < len_B:
        if A[ai] == B[bi]:
            result.append(A[ai])
            ai, bi = ai + 1, bi + 1
        elif A[ai] > B[bi]:
            bi += 1
        else:
            ai += 1

    return result


a, b = [1, 1, 2, 3, 5, 5], [2, 2, 3, 4, 5, 7]
assert get_common_elements(a, b) == [2, 3, 5]
