'''
32. Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/description/

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring

Examples:
1. '(()' -> 2
    Explanation: The longest valid parentheses substring is '()'.

2. ')()())' -> 4
    Explanation: The longest valid parentheses substring is '()()'.

3. '' -> 0
'''

def longestValidParentheses(s: str) -> int:
    stack = [-1]
    max_so_far = 0

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_so_far = max(max_so_far, i - stack[-1])
    
    return max_so_far

def longestValidParentheses_v2(s: str) -> int:
    match_marks = [0] * len(s)     # 0: no match, 1: match found
    stack = []      
    max_length = 0 

    # First pass: mark matching parentheses
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)     # '(' not matched yet, push to stack
        elif stack:
            match_i = stack.pop() 
            match_marks[match_i] = 1   # Mark the position of matched '(' as 1
            match_marks[i] = 1         # Mark the position of matched ')' as 1

    # Second pass: find the longest consecutive ones
    current_length, max_length = 0, 0
    for mark in match_marks:
        if mark == 1:
            current_length += 1 
            max_length = max(max_length, current_length)
        else:
            current_length = 0 

    return max_length
