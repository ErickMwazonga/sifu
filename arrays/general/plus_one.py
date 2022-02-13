'''
Given a non-empty array of digits representing
a non-negative integer,plus one to the integer.
The digits are stored such that the most significant digit 
is at the head of the list, and each element in the 
array contain a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.
# input -> Output
# [1, 2, 3] -> [1, 2, 4]
# [9, 9] -> [1, 0, 0]
'''


def plus_one(arr):
    _str = ''.join(map(str, arr))
    res = str(int(_str) + 1)
    return [int(x) for x in res]


assert plus_one([1, 2, 3]) == [1, 2, 4]
assert plus_one([9, 9, 9]) == [1, 0, 0, 0]
assert plus_one([1, 9, 9]) == [2, 0, 0]


def plus_one_iteratively(arr):
    n = len(arr)

    for i in range(n-1, -1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        arr[i] = 0

    res = [0] * (n + 1)
    res[0] = 1
    return res


assert plus_one_iteratively([1, 2, 3]) == [1, 2, 4]
assert plus_one_iteratively([9, 9, 9]) == [1, 0, 0, 0]
assert plus_one_iteratively([1, 9, 9]) == [2, 0, 0]


def plus_one(digits):
    '''
    digits = [2, 1, 6] -> [2, 1, 7]
    digits = [3, 6, 9, 9] -> [3, 7, 0, 0]
    digits = [9, 9, 9, 9] -> [1, 0, 0, 0, 0]
    '''
    i = len(digits) - 1

    while i >= 0:
        digits[i] += 1

        if digits[i] != 10:
            break
        else:
            digits[i] = 0
            i -= 1

    if i == -1:
        digits.insert(0, 1)

    return digits


def plus_one(A):
    A[-1] += 1

    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A
