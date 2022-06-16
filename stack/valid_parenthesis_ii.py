'''
678. Valid Parenthesis String
Link: https://leetcode.com/problems/valid-parenthesis-string/
Resource: https://bit.ly/3wC0ItI

Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid.
We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single
 left parenthesis '(' or an empty string.
An empty string is also valid.

Examples
1. '()' -> True
2. '(*)' -> True
3. '(*))' -> True

The idea is to check if there is any point violating the rule of valid parenthesis.
In other words, from left to right, any point in the middle should have
#left brackets + #stars >= #right brackets
The same principles apply when
start from right to left, any point in the middle
#right brackets + #stars >= #left brackets
'''


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


def is_valid_v2(s):
    '''Time complexity: O(N), Space complexity: O(N)'''

    left, stars = [], []

    for i, ch in enumerate(s):
        if ch == '*':
            stars.append(i)
        elif ch == '(':
            left.append(i)
        else:
            if not left and not stars:
                return False

            if len(left) > 0:
                left.pop()
            else:
                stars.pop()

    while len(left) > 0 and len(stars) > 0:
        if left.pop() > stars.pop():
            return False

        # if left[-1] > stars[-1]:
        #     return False

        # left.pop()
        # stars.pop()

    return len(left) == 0


assert is_valid('()') == True
assert is_valid('(') == False
assert is_valid('(*)') == True
assert is_valid('(*))') == True
assert is_valid('(*)))') == False
assert is_valid('(*()') == True
assert is_valid(')(') == False


def checkValidString(self, s):
    '''
    :type s: str
    :rtype: bool
    '''
    # stack 1, try to test all the ( and * can balance all the )
    S = []
    # go through s from left to right
    for x in s:
        if x == '(' or x == '*':
            S.append(x)
        else:
            if len(S) > 0:
                S.pop()
            else:
                return False        # this means left ( is not enough

    # stack 2, try to test all the ) and * can balance all the (
    S = []
    # go through s from right to left
    for x in s[::-1]:
        if x == ')' or x == '*':
            S.append(x)
        else:
            if len(S) > 0:
                S.pop()
            else:
                return False        # this means right ) is not enough

    return True
