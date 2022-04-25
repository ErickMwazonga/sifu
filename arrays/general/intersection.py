'''
Write a program to find the sorted non-repeating intersection of
two sorted arrays one x elements long and another y elements long.
The input data consists of two lines of comma separated characters.

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

Examples
input
a, b, c, d, e, f, g, h, i
d, g, i, j, k, l, m

output
d, g, i
'''


def intersection(array1, array2):
    '''O(N + M)'''

    n_array1, n_array2 = len(array1), len(array2)

    i, j = 0, 0
    intersection = []

    while i < n_array1 and j < n_array2:
        if array1[i] == array2[j]:
            if i == 0 or array1[i] != array1[i - 1]:
                intersection.append(array1[i])
                i += 1
                j += 1
        elif array1[i] > array2[j]:
            j += 1
        else:
            i += 1

    return intersection


array1 = 'a, b, c, d, e, f, g, h, i'.split(',')
array2 = 'd, g, i, j, k, l, m'.split(',')

assert intersection(array1, array2) == ['d', 'g', 'i']
