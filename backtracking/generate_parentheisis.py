'''
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/submissions/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Examples
1. 3 -> ["((()))","(()())","(())()","()(())","()()()"]
2. 1 ->  ["()"]
'''


class Solution:
    def generateParenthesis(self, n: int):
        # only add open paranthesis if open < n
        # only ad closing parenthesis if closed < open
        # valid IFF open == closed == n

        res, stack = [], []

        self.backtrack(n, res, stack, openN=0, closedN=0)
        return res

    def backtrack(self, n, res, stack, openN, closedN):
        if openN == closedN == n:
            res.append(''.join(stack))
            return

        if openN < n:
            stack.append('(')
            self.backtrack(n, res, stack, openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(')')
            self.backtrack(n, res, stack, openN, closedN + 1)
            stack.pop()
