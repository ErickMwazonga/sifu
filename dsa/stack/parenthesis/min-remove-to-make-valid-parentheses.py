'''
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 
Example 1:
Input: s = 'lee(t(c)o)de)'
Output: 'lee(t(c)o)de'
Explanation: 'lee(t(co)de)' , 'lee(t(c)ode)' would also be accepted.

Example 2:
Input: s = 'a)b(c)d'
Output: 'ab(c)d'

Example 3:
Input: s = '))(('
Output: ''
Explanation: An empty string is also valid.
'''

def minRemoveToMakeValid(s: str) -> str:
    # clean obvious brackets -> with open and closing + closing bracket when stack is empty
    string_chars, stack = list(s),  []
    for i, ch in enumerate(string_chars):
        if ch == '(':
            stack.append(i)
        if ch == ')':
            if not stack:
                string_chars[i] = ''
            else:
                stack.pop()

    # remove remaining open brackets
    while stack:
        string_chars[stack.pop()] = ''

    return ''.join(string_chars)