'''
Minimum rotations required to get the same string
Given a string, we need to find the minimum number of rotations required to get the same string.

Examples
1. 'geeks' -> 5
2. 'aaaa' -> 1
'''


def findRotations(s):
    # tmp is the concatenated string.
    tmp = s + s
    n = len(s)

    for i in range(1, n + 1):
        # substring from i index of original string size.
        substring = tmp[i: n]

        # if substring matches with original string then we will
        # come out of the loop.
        if s == substring:
            return i

    return n


def findRotations_v2(_str):
    check = ''
    n = len(_str)

    for i in range(1, n + 1):
        check = _str[i:] + _str[:i]

        if check == _str:
            return i
