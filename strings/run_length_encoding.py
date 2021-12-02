'''
Run-length encoding

https://javascript.plainenglish.io/amazon-coding-interview-questions-187eaf91f194

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string 'AAAABBBCCDAA' would be encoded as '4A3B2C1D2A'.

Implement run-length encoding and decoding. You can assume the string to be encoded have
no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.

Encode:
Input: "WWWWWWWWWBBBBBBB"
Output: "9W7B"

Decode:
Input "9W7B"
Output: "WWWWWWWWWBBBBBBB"
'''


def encode(_str):
    n = len(_str)

    if _str == _str[0] * n:
        return f'{n}{_str[0]}'

    i, _count = 1, 1
    encoding = ''

    while i < n:
        if _str[i] == _str[i-1]:
            _count += 1
        else:
            encoding += f'{_count}{_str[i-1]}'
            _count = 1

        i += 1

    encoding += f'{_count}{_str[i-1]}'  # last iteration

    return encoding


def decode(_str):
    n = len(_str)
    decoding = ''

    for i in range(1, n, 2):
        decoding += int(_str[i-1]) * _str[i]

    return decoding


assert encode('WWWWWW') == '6W'
assert encode('WWWWWWWWWBBBBBBB') == '9W7B'
assert encode('WWWWWWWWWBBBBBBBR') == '9W7B1R'
assert encode('W') == '1W'

assert decode('9W7B') == 'WWWWWWWWWBBBBBBB'
assert decode('1W7B') == 'WBBBBBBB'
assert decode('9W1B') == 'WWWWWWWWWB'
assert decode('1W1B') == 'WB'
assert decode('0W1B') == 'B'
assert decode('1W0B') == 'W'
assert decode('0W0B') == ''
assert decode('1A1B1C') == 'ABC'
assert decode('1A1B') == 'AB'
