'''
709. To Lower Case
https://leetcode.com/problems/to-lower-case/

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Examples
1. 'Hello' -> 'hello'
2. 'here' -> 'here'
3. 'LOVELY' -> 'lovely'
'''


def toLowerCase(self, str):
    lowered = []
    for i in str:
        char_code = ord(i)
        # if A-Z
        if char_code < 91 and char_code > 64:
            lowered += chr(char_code + 32)
        else:
            lowered += i

    return ''.join(lowered)


def toLowerCase_v2(self, str: str) -> str:
    res = ''

    for i in range(len(str)):
        if(ord(str[i]) >= 65 and ord(str[i]) <= 90):
            res += chr(ord(str[i])+32)
        else:
            res += str[i]

    return res


assert toLowerCase('Hello') == 'hello'
assert toLowerCase('here') == 'here'
assert toLowerCase('LOVELY') == 'lovely'
