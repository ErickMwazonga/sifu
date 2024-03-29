'''
20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

1. '()' -> true
2. '()[]{}' -> true
3. '(]' -> false
4. '([)]' -> false
5. '{[]}' -> true
'''


def is_valid(_str: str) -> bool:
    stack = []
    matches = {'(': ')', '[': ']', '{': '}'}

    for char in _str:
        if char in matches:
            stack.append(char)
        else:
            if not stack:
                return False

            last_open_bracket = stack.pop()
            if matches[last_open_bracket] != char:
                return False

    return not stack


def is_valid_v2(s):
    '''GLOVO INTERVIEW'''

    if not s:
        return True

    if len(s) % 2 != 0:
        return False

    matches = {')': '(', '}': '{', ']': '['}
    stack = []

    for bracket in s:
        if not stack:
            stack.append(bracket)
        else:
            if bracket not in matches:
                stack.append(bracket)
            else:
                last = stack.pop()
                if bracket not in matches or matches[bracket] != last:
                    return False

    return len(stack) == 0


assert is_valid(']') is False
assert is_valid('()') is True
assert is_valid('()[]{}') is True
assert is_valid('(]') is False
assert is_valid('([)]') is False
assert is_valid('{[]}') is True
