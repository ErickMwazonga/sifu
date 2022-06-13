'''
1249. Minimum Remove to Make Valid Parentheses
Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Intuition: https://bit.ly/3LBJlxp

Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Examples:
1. 'lee(t(c)o)de)' -> 'lee(t(c)o)de'
Explanation: 'lee(t(co)de)' , 'lee(t(c)ode)' would also be accepted.

2. 'a)b(c)d' -> 'ab(c)d'
3. '))((' ->  ''
Explanation: An empty string is also valid
'''


def minRemoveToMakeValid(s):
    s, stack = list(s), []

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''

    while stack:
        popped = stack.pop()
        s[popped] = ''

    return ''.join(s)
