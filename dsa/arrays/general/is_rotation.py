'''
Check is one array is a rotation of the other

NB:
No duplicates

A - [1, 2, 3, 4, 5, 6, 7]
B - [4, 5, 6, 7, 1, 2, 3]

Output - True

INTUITION
Normal element index = i
Rotated element index = (i + k) % n
    where: n - no of elements, k - offset
'''


def is_rotation(A, B):
    n, m = len(A), len(B)

    if n != m:
        return False

    offset = -1
    first_char = A[0]

    for i, num in enumerate(B):
        if first_char == num:
            offset = i
            break

    if offset == -1:
        return False

    for i in range(n):
        key = (i + offset) % n
        if A[i] != B[key]:
            return False

    return True

A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 1, 2, 3]
assert is_rotation(A, B) == True
