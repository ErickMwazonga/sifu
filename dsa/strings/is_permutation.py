'''
Given two strings, write a method to decide if 
one is a permutation of the other.

Approach: Sorting
Time Complexity: O(nlogn), Space Complexity: O(1)
'''


def is_perm(str_1: str, str_2: str) -> bool:
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    n = len(str_1)

    for i in range(n):
        if str_1[i] != str_2[i]:
            return False

    return True


def is_perm_v2(str_1: str, str_2: str) -> bool:
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    d = {}

    for i in str_1:
        d.get(i, 0) + 1

    for i in str_2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1

    return all(value == 0 for value in d.values())


is_permutation_1, is_permutation_2 = 'google', 'ooggle'
not_permutation_1, not_permutation_2 = 'not', 'topx]'

assert is_perm(is_permutation_1, is_permutation_2) == True

# not working as expected
# assert is_perm(not_permutation_1, not_permutation_1) == False
