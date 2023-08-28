def convert_number_to_readable_digit_v1(number: int) -> str:
    return f'{number:,}'

def convert_number_to_readable_digit_v2(number: int) -> str:
    result = []
    number_as_string = reversed(str(number))

    for i, ch in enumerate(number_as_string):
        if i != 0 and i % 3 == 0: 
            result.append(',')
        
        result.append(ch)

    return ''.join(reversed(result))

def convert_number_to_readable_digit_v3(number: int) -> str:
    number_as_string = str(number)
    groups = []

    while number_as_string:
        groups.append(number_as_string[-3:])
        number_as_string = number_as_string[:-3]

    return ','.join(reversed(groups))


test_cases = {
    '100000000': '100,000,000',
    '1234567890': '1,234,567,890',
}

for _input, output in test_cases.items():
    assert convert_number_to_readable_digit_v1(int(_input)) == output
    assert convert_number_to_readable_digit_v2(int(_input)) == output
    assert convert_number_to_readable_digit_v3(int(_input)) == output