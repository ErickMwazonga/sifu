"""
https://leetcode.com/problems/valid-parenthesis-string/
678. Valid Parenthesis String
Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid.
We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Input: "()" -> Output: True
Input: "(*)" -> Output: True
Input: "(*))" -> Output: True

The idea is to check if there is any point violating the rule of valid parenthesis.
In other words, from left to right, any point in the middle should have
#left brackets + #stars >= #right brackets
The same principles apply when
start from right to left，any point in the middle
#right brackets + #stars >= #left brackets
"""

def is_valid(s):
    left, star, right = 0, 0, 0

    for c in s:
        if c == '(':
            left += 1
        elif c == '*':
            star += 1
        else:
            right += 1
        if left + star < right:
            return False
        
    left, star, right = 0, 0, 0
    for c in s[::-1]:
        if c == '(':
            left += 1
        elif c == '*':
            star += 1
        else:
            right += 1
        if right + star < left:
            return False
    return True

    # if stars_count >= unmatched_brackets_count:
    #     return True
    # return False

    # custom_stack = []
    # stars_seen = 0

    # for char in str:
    #     if char == '*':
    #         stars_seen += 1

    #     if char == '(':
    #         custom_stack.append(char)

    #     elif char == ')':
    #         if not custom_stack:
    #             custom_stack.append(char)
    #         else:
    #             custom_stack.pop()

    # print(stars_seen, len(custom_stack))

    # if stars_seen >= len(custom_stack):
    #     return True
    # return False

    # return '(' not in custom_stack


assert is_valid('()') == True
assert is_valid('(') == False
assert is_valid('(*)') == True
assert is_valid('(*))') == True
assert is_valid('(*)))') == False
assert is_valid('(*()') == True
assert is_valid(')(') == False
