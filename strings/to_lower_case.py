'''
709. To Lower Case
Link: https://leetcode.com/problems/to-lower-case/

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Examples
1. 'Hello' -> 'hello'
2. 'here' -> 'here'
3. 'LOVELY' -> 'lovely'
'''


def toLowerCase(str):
    lowered = []

    for ch in str:
        char_code = ord(ch)
        # if A-Z
        if char_code < 91 and char_code > 64:
            lowered += chr(char_code + 32)
        else:
            lowered += ch

    return ''.join(lowered)


def toLowerCase_v2(str: str) -> str:
    res = ''

    for ch in str:
        val = ord(ch)

        if(65 <= val <= 90):  # if (ord(ch) >= 65 and ord(ch) <= 90):
            res += chr(val + 32)
        else:
            res += str[ch]

    return res


assert toLowerCase('Hello') == 'hello'
assert toLowerCase('here') == 'here'
assert toLowerCase_v2('LOVELY') == 'lovely'
