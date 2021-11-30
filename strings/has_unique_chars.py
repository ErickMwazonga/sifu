'''
Implement an algorithm to determine if a string has all
unique characters.
'''


def is_unique_1(input_str):
    _hash = {}

    for char in input_str:
        if char in _hash:
            return False
        _hash[char] = 1
    return True


def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)


def is_unique_3(input_str):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, '')
        else:
            return False
    return True


unique_str = 'AbCDefG'
non_unique_str = 'non Unique STR'

assert is_unique_1(unique_str) == True
assert is_unique_1(non_unique_str) == False

assert is_unique_2(unique_str) == True
assert is_unique_2(non_unique_str) == False

assert is_unique_3(unique_str) == True
assert is_unique_3(non_unique_str) == False
