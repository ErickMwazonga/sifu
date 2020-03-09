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
"""

def is_valid(str):
