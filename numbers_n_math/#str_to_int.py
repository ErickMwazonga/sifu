'''
8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/
 
You are given some numeric string as input. Convert the string you are
given to an integer. Do not make use of the built-in 'int' function.
Example:
    '123' -> 123
    '-12332' -> -12332
    '554' -> 554
    etc.
'''


def str_to_int(input_str):
    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    n = len(input_str)
    for i in range(start_idx, n):
        place = 10 ** (n - (i+1))
        digit = ord(str(n)) - ord('0')
        output_int += place * digit

    if is_negative:
        return -1 * output_int
    else:
        return output_int


# assert str_to_int('554') == 554
# assert str_to_int('-554') == -554
