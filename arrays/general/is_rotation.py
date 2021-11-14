'''
Check is one array is a rotation of the other

NB:
No duplicates

A - [1, 2, 3, 4, 5, 6, 7]
B - [4, 5, 6, 7, 1, 2, 3]

Output - True
'''


def is_rotation(A, B):
    len_A, len_B = len(A), len(B)

    if len_A != len_A:
        return False

    # Find the index of the first num of A in B
    a = A[0]
    ai = -1

    for i, num in enumerate(B):
        if a == num:
            ai = i

    # First num in A is not in B
    if ai == -1:
        return False

    for i in range(1, len_A):
        j = (ai + 1) % len_B
        ai += 1

        if A[i] != B[j]:
            return False

    return True


A = [1, 2, 3, 4, 5, 6, 7]
B = [4, 5, 6, 7, 1, 2, 3]
assert is_rotation(A, B) == True
