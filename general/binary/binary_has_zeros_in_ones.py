"""
Given a string of 0 and 1, we need to check that the given string is valid or not.
The given string is valid when there is no zero is present in between 1’s.
For example, 1111, 0000111110, 1111000 are valid strings but 01010011, 01010, 101 are not.
https://www.geeksforgeeks.org/check-binary-string-0-1s-not-set-2-regular-expression-approach/
"""


def has_zeros_in_ones(binary):
    if len(set(binary)) == 1:
        return 'VALID'

    ones_first_index = binary.find('1')
    ones_last_index = binary.rfind('1')

    if ones_first_index != -1 and ones_last_index != -1:
        found_zero = binary.find('0', ones_first_index, ones_last_index)

        if found_zero != -1:
            return 'INVALID'

    return 'VALID'


# For example, 1111, 0000111110, 1111000 are valid strings but 01010011, 01010, 101 are not.
# print(has_zeros_in_ones('1111'))
# print(has_zeros_in_ones('0000111110'))
print(has_zeros_in_ones('01010011'))
