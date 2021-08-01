'''
Check if N and its Double exits
'''


def checkExists(arr):
    _hash = set(arr)

    for num in arr:
        half, double = num / 2, num * 2

        if half in _hash or double in _hash:
            return True

    return False


assert checkExists([2, 5, 6, 4, 9]) == True
assert checkExists([8, 5, 6, 4, 1]) == True
assert checkExists([13, 5, 6, 4, 1]) == False
