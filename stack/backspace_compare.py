'''
LeetCode 844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when
both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = 'ab#c', T = 'ad#c'
Output: true -> Explanation: Both S and T become 'ac'.

Example 2:
Input: S = 'ab##', T = 'c#d#'
Output: true -> Explanation: Both S and T become ''.

Example 3:
Input: S = 'a##c', T = '#a#c'
Output: true -> Explanation: Both S and T become 'c'.

Example 4:
Input: S = 'a#c', T = 'b'
Output: false -> Explanation: S becomes 'c' while T becomes 'b'.
'''


def helper(S):
    _stack = []

    for c in S:
        if c != '#':
            _stack.append(c)
        else:
            if _stack:
                _stack.pop()

    return ''.join(_stack)


def backspaceCompare(S: str, T: str) -> bool:
    '''Time complexity: O(n), Space complexity: O(n).'''

    return helper(S) == helper(T)


assert backspaceCompare('ab#c', 'ad#c') == True
assert backspaceCompare('ab##', 'c#d#') == True
assert backspaceCompare('a##c', '#a#c') == True
assert backspaceCompare('a#c', 'b') == False
