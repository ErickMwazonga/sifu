'''
Implement an algorithm to determine if a string has all unique characters.
'''


def is_unique(_input: str) -> bool:
    _hash = {}

    for char in _input:
        if char in _hash:
            return False
        _hash[char] = 1

    return True


def is_unique_v2(_input: str) -> bool:
    return len(set(_input)) == len(_input)


def is_unique_v3(_input: str) -> bool:
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for i in _input:
        if i in alpha:
            alpha = alpha.replace(i, '')
        else:
            return False
    return True


unique_str = 'AbCDefG'
non_unique_str = 'non Unique STR'

assert is_unique(unique_str) == True
assert is_unique(non_unique_str) == False

assert is_unique_v2(unique_str) == True
assert is_unique_v2(non_unique_str) == False

assert is_unique_v3(unique_str) == True
assert is_unique_v3(non_unique_str) == False
