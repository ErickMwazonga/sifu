'''
LeetCode 844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when
both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true -> Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true -> Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true -> Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false -> Explanation: S becomes "c" while T becomes "b".
'''

 def backspaceCompare(self, S: str, T: str) -> bool:
    '''
    Time complexity: O(n), Space complexity: O(n).
    '''
    S_stack, T_stack = [], []
    
    for c in S:
        if c != '#':
            S_stack.append(c)
        else:
            if S_stack:
                S_stack.pop()
                
    for c in T:
        if c != '#':
            T_stack.append(c)
        else:
            if T_stack:
                T_stack.pop()
                
    return ''.join(S_stack) == ''.join(T_stack)