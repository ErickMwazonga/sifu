'''
You are given some integer as input, (i.e. ... -3, -2, -1, 0, 1, 2, 3 ...)
Convert the integer you are given to a string. Do not make use
of the built-in 'str' function.

Examples:
1. 123 -> '123'
2. -123 -> '-123'
'''


def int_to_str(input_int: int) -> str:
    is_negative = input_int < 0

    if is_negative:
        input_int *= -1

    output_str = []
    while input_int > 0:
        input_int, remainder = divmod(input_int, 10)
        val_repr = ord('0') + remainder
        char_rep = chr(val_repr)
        output_str.append(char_rep)

    output_str = output_str[::-1]
    output_str = ''.join(output_str)

    return '-' + output_str if is_negative else output_str


assert int_to_str(123) == '123'
assert int_to_str(-123) == '-123'
